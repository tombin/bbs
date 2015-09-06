import re
from getpass import getpass
from passlib.hash import sha256_crypt

class Login():
    def __init__(self):
        self.config = {}
        with open("config", "r") as fd:
            for line in fd:
                line = line.strip('\n')
                (option, value) = line.split(':', 1)
                self.config[option] = value 

    def getUser(self):
        for tryLogin in range(0, int(self.config['tryLogin'])):
            username = raw_input(self.config['loginPrompt'])
            username = username.strip('\n')
            username = re.sub(r'[^A-Za-z0-9_.-]', '', username)
            if self.checkUser(username):
                print self.config['welcomeUsername']
                return username 
            else:
                print self.config['invalidUsernamePassword']
        print self.config['tooManyLoginTry']
        return False

    def checkUser(self, username):
        passwdFile = {}   
        enteredPw = getpass(self.config['passwdPrompt'])     
        with open("passwd", "r") as fd:
            for line in fd:
                (user, passwd) = line.split(':')
                passwdFile[user] = passwd
        if username in passwdFile.keys() and self.checkPasswd(passwdFile[username], enteredPw):
            return True
        else:
            return False
 
    def checkPasswd(self, passwd, enteredPw):
        passwd = passwd.strip('\n')
        if sha256_crypt.verify(enteredPw, passwd):
            return True
        else:
            return False


