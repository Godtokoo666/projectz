import threading
import socket
from db_op import *
import time

class GroupChat (threading.Thread):
    def __init__(self, port):
        '''初始化'''
        threading.Thread.__init__(self)
        self.port = port
        self.sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dbq=DataBaseQueryer('D:\Python_Workspace\Server\chat.db')
        self.dbo=DataBaseOperator('D:\Python_Workspace\Server\chat.db')
        self.onlineusers=[set() for _ in range(10)] #在线用户列表,每个群组一个set:set为无序不重复元素集，range的参数为群组数
        self.updatamainlist()
        self.connect=[[]for i in range(10)] #连接列表，每个群组一个列表，列表里均为socket对象，range的参数为群组数
    def boardcastmsg(self,gid:int,message:str): #已弃用
        '''广播消息'''
        message='newmes'+','+message
        for i in self.connect[gid]:
            i.send(message.encode('utf-8'))

    def getChatList(self,gid:int): #初始化消息列表，被intimessage调用
        '''获取聊天记录'''
        return self.dbq.ChatListQuery(gid)

    def connect_handler(self, conn, addr): #多线程处理连接
        '''连接处理'''
        username=''
        group=''
        loginstatus=False #登录状态
        try:
            while True:
                data = conn.recv(1024).decode('utf-8').split(',')
                print(data)
                if data[0]=='mes': #消息处理
                    self.dbo.addChatCotent(self.groupmap[data[1]],self.usermap[data[2]],data[3])
                    self.sendall('newmes',data[1],data[2],data[3])
                elif data[0]=='login':  #登录处理
                    loginstatus=self.handlelogin(conn,data[1],data[2])
                    if loginstatus:
                        username=data[1]
                        group=self.getusergroup(data[1])
                        self.updateonlinelist('newusr',group,username) #更新在线用户列表
                        username=data[1]
                        self.initmessage(conn,group) #为当前用户初始化消息，并把更新后的在线用户列表发给所有用户
                elif data[0]=='preregister':
                    conn.send(str(self.groupList).encode('utf-8')) #预注册处理，发送群组列表给客户端，作为注册时的下拉框选项
                elif data[0]=='register':   #注册处理
                    self.handleregister(conn,data[1],data[2],data[3])
                elif data[0] == 'refresh':  #刷新处理
                    self.handlerefresh(conn,data[1])
        except Exception as e:
            print(e)
        finally:
            '''关闭连接，更新在线用户列表'''
            if loginstatus:
                try:
                    self.connect[self.groupmap[group]].remove(conn) #删除socket对象
                except Exception as e:
                    print("Client has been forced to close")
                self.updateonlinelist('delusr',group,username) #更新在线用户列表
                self.sendall('onuser',group,username,str(self.onlineusers[self.groupmap[group]])) #发送更新后的在线用户列表给所有用户
            conn.close()

    def handlelogin(self,conn,username,password):
        '''处理登录'''
        cpass=self.dbq.passwordQuery(username)
        if cpass and cpass[0][0] == password:
            result='login'+','+'True'
            conn.send(result.encode('utf-8'))
            return True
        else :
            result='login'+','+'False'
            conn.send(result.encode('utf-8'))
            return False

    def initmessage(self,conn,group):
        '''初始化消息'''
        self.connect[self.groupmap[group]].append(conn)
        res=group+'*'+str(self.userlist)+'*'+str(self.onlineusers[self.groupmap[group]])+'*'+str(self.getChatList(self.groupmap[group])) 
        '''
        此处初始化消息，发送给客户端的消息格式为：
        group*userlist*onlineusers*chatlist
        客户端收到后，用*分割，分别赋值给group,userlist,onlineusers,chatlist
        初始化的消息逻辑是把数据库所有的聊天记录都发给客户端，
        客户端收到后，用for循环遍历，把每条消息都显示出来
        但当数据库聊天记录过多时，这样写可能会超过socket的字节数限制，
        导致消息发送失败，后续可改为只把最近的10条消息发给客户端
        '''
        conn.send(res.encode('utf-8'))
        time.sleep(2) #等待2秒，等待客户端初始化消息，防止socket连续接收消息导致消息混乱
        self.sendall('onuser',group,1,str(self.onlineusers[self.groupmap[group]]))
    
    def updatamainlist(self):
        '''更新用户、群组列表，被注册和初始化时调用'''
        self.userlist=self.dbq.UserListQuery() #获取用户列表 [(uid,username,gid)]
        self.groupList=self.dbq.GroupListQuery() #获取群组列表 [(gid,gname)]
        self.usermap={}
        self.groupmap={}
        for i in self.userlist: #建立用户映射 {username:uid}
            self.usermap[i[1]]=i[0]
        for i in self.groupList:    #建立群组映射 {gname:gid}
            self.groupmap[i[1]]=i[0]
        
    def getusergroup(self,username):
        '''获取用户所在群组'''
        UserGroup=self.dbq.UserGroupQuery(username) #获取用户所在群组 [(gid,)]
        group=self.groupList[UserGroup[0][0]-1][1] #str
        return group

    def handleregister(self,conn,username,password,group):
        '''处理注册'''
        if self.usermap.get(username)==None:
            self.dbo.addUser(username,password,self.groupmap[group],'1') #向数据库添加用户
            self.updatamainlist() #更新用户、群组列表，防止注册后，其他用户调用userlist时，出现index out of range
            result='register'+','+'True'
            conn.send(result.encode('utf-8'))
            time.sleep(2)
            self.sendall('updatemainlist',group,1,str(self.userlist)) #发送更新后的用户列表给所有用户
        else:
            result='register'+','+'False'
            conn.send(result.encode('utf-8'))

    def handlerefresh(self,conn,group):
        '''处理刷新
        由于消息为增量更新，而且本项目中socket是基于TCP的，
        所以刷新时，只需要把在线用户列表发给客户端即可
        '''
        res='onuser'+','+str(self.onlineusers[self.groupmap[group]])
        conn.send(res.encode('utf-8'))

    def sendall(self, type, group,username, message):
        '''群发消息'''
        if type=='onuser': #更新在线用户列表
            message=('onuser'+','+message).encode('utf-8')
            for i in self.connect[self.groupmap[group]]:
                i.send(message)
        elif type=='newmes': #发送消息，消息的直接来源不来自数据库，而是来自某一客户端
            message=('newmes'+','+username+','+message).encode('utf-8')
            for i in self.connect[self.groupmap[group]]:
                i.send(message)
        elif type=='updatemainlist': #更新用户列表，用于注册后，更新所有用户的用户列表
            message='mainlist'+','+str(self.userlist)
            for i in self.connect[self.groupmap[group]]:
                i.send(message.encode('utf-8'))

    def updateonlinelist(self,type,group,username):
        '''更新在线用户列表'''
        if type=='newusr':
            self.onlineusers[self.groupmap[group]].add(username)
        else:
            self.onlineusers[self.groupmap[group]].remove(username)

    def run(self):
        '''运行'''
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(128) #监听，128为最大连接数
        print("Server is running on port %d" % self.port)
        while True:
            conn, addr = self.sock.accept()
            t=threading.Thread(target=self.connect_handler, args=(conn, addr)) #多线程处理连接
            t.start()
  
if  __name__ == "__main__":
    port = 8099
    groupChat=GroupChat(port)
    groupChat.run()
    groupChat.sock.close()