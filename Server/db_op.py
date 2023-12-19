import sqlite3

class DataBaseOperator:
    '''数据库操作类'''
    def __init__(self,dbName:str):
        self.dbName=dbName
        self.conn = sqlite3.connect(self.dbName, check_same_thread=False, timeout=2.0)
        self.cursor = self.conn.cursor()
    def dbInit(self): #数据库初始化
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (uid INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,role TEXT,gid INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS groups (gid INTEGER PRIMARY KEY AUTOINCREMENT,gname TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (cid INTEGER PRIMARY KEY AUTOINCREMENT,gid INTEGER,uid INTEGER,content TEXT)")
        self.conn.commit()
    def addUser(self,username:str,password:str,role:str,gruop:int): #添加用户
        self.cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",(None,username,password,role,gruop))
        self.conn.commit()
    def addGroup(self,gid:int,gname:str): #添加群组
        self.cursor.execute("INSERT INTO groups VALUES (?,?)",(gid,gname))
        self.conn.commit()
    def addChatCotent(self,gid:int,uid:int,content:str): #添加消息
        self.cursor.execute("INSERT INTO chat VALUES (?,?,?,?)",(None,gid,uid,content))
        self.conn.commit()
        
class DataBaseQueryer:
    '''数据库查询类'''
    def __init__(self,dbName:str):
        self.dbName=dbName
        self.conn = sqlite3.connect(self.dbName, check_same_thread=False, timeout=2.0)
        self.cursor = self.conn.cursor()
    def GroupListQuery(self): #查询群组列表
        self.cursor.execute("SELECT gid,gname FROM groups")
        return self.cursor.fetchall()
    def UserListQuery(self): #查询用户列表
        self.cursor.execute("SELECT uid,username,gid FROM users")
        return self.cursor.fetchall()
    def ChatListQuery(self,gid:int): #查询聊天记录
        self.cursor.execute("SELECT * FROM chat WHERE gid=?",(gid,))
        return self.cursor.fetchall()
    def UserGroupQuery(self,username:str): #查询用户所在群组
        self.cursor.execute("SELECT gid FROM users WHERE username=?",(username,))
        return self.cursor.fetchall() #[(gid,)]
    def passwordQuery(self,username:str): #查询用户密码
        self.cursor.execute("SELECT password FROM users WHERE username=?",(username,))
        return self.cursor.fetchall()

# if __name__ == '__main__':
#     dbc=DataBaseOperator('D:\Python_Workspace\Server\chat.db')
#     dbc.dbInit()
#     dbc.addUser(1,'admin','admin',0,'admin')
#     dbc.addGroup(2,'Group2')
#     dbc.addChatCotent(2,1,'I love Python')
#     dbq=DataBaseQueryer('D:\Python_Workspace\Server\chat.db')
#     print(dbq.ChatListQuery(1))