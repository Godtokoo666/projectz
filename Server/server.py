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
        self.onlineusers=set()
        self.userlist=self.dbq.UserListQuery() #获取用户列表 [(uid,username,gid)]
        self.groupList=self.dbq.GroupListQuery() #获取群组列表 [(gid,gname)]
        self.usermap={}
        self.groupmap={}
        for i in self.userlist: #建立用户映射 {username:uid}
            self.usermap[i[1]]=i[0]
        for i in self.groupList:    #建立群组映射 {gname:gid}
            self.groupmap[i[1]]=i[0]
        self.connect=[[]for i in range(10)]
    def boardcastmsg(self,gid:int,message:str):
        '''广播消息'''
        message='newmes'+','+message
        for i in self.connect[gid]:
            i.send(message.encode('utf-8'))

    def getChatList(self,gid:int):
        '''获取聊天记录'''
        return self.dbq.ChatListQuery(gid)

    def connect_handler(self, conn, addr):
        '''连接处理'''
        username=''
        group=''
        loginstatus=False
        try:
            while True:
                data = conn.recv(1024).decode('utf-8').split(',')
                print(data)
                if data[0]=='mes': #消息处理
                    self.dbo.addChatCotent(self.groupmap[data[1]],self.usermap[data[2]],data[3])
                    self.sendall('newmes',data[1],data[2],data[3])
                    print("this")
                elif data[0]=='login':  #登录处理
                    loginstatus=self.handlelogin(conn,data[1],data[2])
                    if loginstatus:
                        group=self.getusergroup(data[1])
                        username=data[1]
                        self.initmessage(conn,group)
                elif data[0]=='register':   #注册处理
                    self.handleregister(conn,data[1],data[2],data[3])
                elif data[0] == 'refresh':  #刷新处理
                    self.handlerefresh(conn)
        except Exception as e:
            print(e)
        finally:
            if loginstatus:
                self.connect[self.groupmap[group]].remove(conn)
                self.updateonlinelist('delusr',username) #更新在线用户列表
                print("this")
                self.sendall('onuser',group,username,str(self.onlineusers))
            conn.close()
            

    def handlelogin(self,conn,username,password):
        '''处理登录'''
        cpass=self.dbq.passwordQuery(username)
        if cpass and cpass[0][0] == password:
            result='login'+','+'True'
            conn.send(result.encode('utf-8'))
            self.updateonlinelist('newusr',username) #更新在线用户列表
            return True
        else :
            result='login'+','+'False'
            conn.send(result.encode('utf-8'))
            return False
    def initmessage(self,conn,group):
        '''初始化消息'''
        self.connect[self.groupmap[group]].append(conn)
        res=group+'*'+str(self.userlist)+'*'+str(self.onlineusers)+'*'+str(self.getChatList(self.groupmap[group])) #初始化消息
        conn.send(res.encode('utf-8'))
        time.sleep(2)
        self.sendall('onuser',group,1,str(self.onlineusers))
        
        
    def getusergroup(self,username):
        '''获取用户所在群组'''
        UserGroup=self.dbq.UserGroupQuery(username) #获取用户所在群组 [(gid,)]
        group=self.groupList[UserGroup[0][0]-1][1] #str
        return group

    def handleregister(self,conn,username,password,group): #未审查To Do
        '''处理注册'''
        if self.usermap.get(username)==None:
            self.dbo.addUser(len(self.userlist)+1,username,password,self.groupmap[group],'user')
            self.updateonlinelist('newusr',username)
            self.sendall('newusr',str(self.onlineusers))
            result='register'+','+'True'
            conn.send(result.encode('utf-8'))
        else:
            result='register'+','+'False'
            conn.send(result.encode('utf-8'))


    def handlerefresh(self,conn):
        '''处理刷新'''
        res='onuser'+','+str(self.onlineusers)
        conn.send(res.encode('utf-8'))

    def sendall(self, type, group,username, message):
        '''群发消息'''
        if type=='onuser':
            message=('onuser'+','+message).encode('utf-8')
            for i in self.connect[self.groupmap[group]]:
                i.send(message)
        elif type=='newmes':
            message=('newmes'+','+username+','+message).encode('utf-8')
            for i in self.connect[self.groupmap[group]]:
                i.send(message)

            
    def updateonlinelist(self,type,username):
        '''更新在线用户列表'''
        if type=='newusr':
            self.onlineusers.add(username)
        else:
            self.onlineusers.remove(username)

    def run(self):
        '''运行'''
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(128)
        print("Server is running on port %d" % self.port)
        while True:
            conn, addr = self.sock.accept()
            t=threading.Thread(target=self.connect_handler, args=(conn, addr))
            t.start()
        
        
        
if  __name__ == "__main__":
    port = 8099
    groupChat=GroupChat(port)
    groupChat.run()
    groupChat.sock.close()