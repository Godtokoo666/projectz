import sqlite3

class DataBaseOperator:
    def __init__(self,dbName:str):
        self.dbName=dbName
        self.conn = sqlite3.connect(self.dbName, check_same_thread=False, timeout=2.0)
        self.cursor = self.conn.cursor()
    def dbInit(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (uid INTEGER PRIMARY KEY,username TEXT,password TEXT,role TEXT,gid INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS groups (gid INTEGER PRIMARY KEY,gname TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (cid INTEGER PRIMARY KEY AUTOINCREMENT,gid INTEGER,uid INTEGER,content TEXT)")
        self.conn.commit()
    def addUser(self,uid:int,username:str,password:str,group:int,role:str):
        self.cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",(uid,username,password,group,role))
        self.conn.commit()
    def addGroup(self,gid:int,gname:str):
        self.cursor.execute("INSERT INTO groups VALUES (?,?)",(gid,gname))
        self.conn.commit()
    def addChatCotent(self,gid:int,uid:int,content:str):
        self.cursor.execute("INSERT INTO chat VALUES (?,?,?,?)",(None,gid,uid,content))
        self.conn.commit()
        
class DataBaseQueryer:
    def __init__(self,dbName:str):
        self.dbName=dbName
        self.conn = sqlite3.connect(self.dbName, check_same_thread=False, timeout=2.0)
        self.cursor = self.conn.cursor()
    def GroupListQuery(self):
        self.cursor.execute("SELECT gid,gname FROM groups")
        return self.cursor.fetchall()
    def UserListQuery(self):
        self.cursor.execute("SELECT uid,username,gid FROM users")
        return self.cursor.fetchall()
    def ChatListQuery(self,gid:int):
        self.cursor.execute("SELECT * FROM chat WHERE gid=?",(gid,))
        return self.cursor.fetchall()
    def UserGroupQuery(self,username:str):
        self.cursor.execute("SELECT gid FROM users WHERE username=?",(username,))
        return self.cursor.fetchall() #[(gid,)]
    def passwordQuery(self,username:str):
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