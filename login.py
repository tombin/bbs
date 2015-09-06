import re
from getpass import getpass
from passlib.hash import sha256_crypt
import user
from user import checkUserExists

class Login:
    def __init__(self):
        pass

    def getUser(self):
        for tryLogin in range(0, int(self.config['tryLogin'])):
            username = raw_input(self.config['loginPrompt'])
            username = username.strip('\n')
            username = re.sub(r'[^A-Za-z0-9_.-]', '', username)
            if username == "new":
                return username
            if self.checkPasswd(username):
                print self.config['welcomeUsername']
                return username 
            else:
                print self.config['invalidUsernamePassword']
        print self.config['tooManyLoginTry']
        return False

    def checkPasswd(self, username):
        passwdFile = {}
        enteredPw = getpass(self.config['passwdPrompt'])
        with open("passwd", "r") as fd:
            for line in fd:
                line = line.strip('\n')
                (user, passwd) = line.split(':')
                passwdFile[user] = passwd
        if checkUserExists(username) and sha256_crypt.verify(enteredPw, passwdFile[username]):
            return True
        else:
            return False

