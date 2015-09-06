from passlib.hash import sha256_crypt
from getpass import getpass
from user import checkUserExists

class Newuser:
    def __init__(self):
        self.username = ""

    def updatePwFile(self):
        pw = getpass(self.config['passwdPrompt'])
        with open("passwd", "a") as fd:
            fd.write(self.username + ":" + sha256_crypt.encrypt(pw) + '\n')

    def getUserInfo(self):
        username = raw_input(self.config['loginPrompt'])
        if checkUserExists(username):
            print self.config['userUnavailable'] 
        else:
            print self.config['userAvailable']
            self.username = username
            self.updatePwFile()


