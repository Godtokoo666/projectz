from groupchat import *
from login import *
from register import *
from privatechat import *

if __name__ == '__main__':
    login = MyLogin()
    if login.run():
        groupchat = MyGroupChat(login.username, login.group)
        groupchat.show()
        sys.exit(app.exec_())