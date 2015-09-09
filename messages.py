import pickle
import sys

class Messages:
    def __init__(self, username=None):
        self.username = username
        self.msgConfig = pickle.load(open("msgconfig", "r"))
        self.userConfig = pickle.load(open(self.username + ".config", "r"))

    def updateUserConfig(self):
        pickle.dump(self.userConfig, open(self.username + ".config", "wb"))
        self.userConfig = pickle.load(open(self.username + ".config", "r"))

    def updateMsgConfig(self):
        pickle.dump(self.msgConfig, open("msgconfig", "wb"))
        self.msgConfig = pickle.load(open("msgconfig", "r")) 

    def readNew(self, msgBase):
        if msgBase not in self.userConfig: 
            self.userConfig['msgbase'][msgBase]['lastRead'] = 0              
        lastRead = int(self.userConfig['msgbase'][msgBase]['lastRead'])
        lastMsg = int(self.msgConfig[msgBase]['totalMsgs'])
        if lastMsg == 0:
            print "No messages"
        else:
            for currentMsg in xrange(lastRead+1, lastMsg+1):
               msgData = pickle.load(open(str(currentMsg) + ".msg"))
               #self.userConfig['msgbase'][msgBase]['lastRead'] = currentMsg
               self.printHeader(msgData['from'], msgData['to'], msgData['subject'])
               print msgData['body']
               self.printFooter()
               #self.updateUserConfig()

    def printHeader(self, _from, _to, _subject):
        print "-" * 80
        print "   From: " + _from
        print "     To: " + _to
        print "Subject: " + _subject
        print "-" * 80
    
    def printFooter(self):
        print "-" * 80

    def saveMsg(self, msgBase, _to, _subject, _body):
        _body = ''.join(_body)
        msgData = {}
        msgData['body'] = _body 
        msgData['subject'] = _subject
        msgData['from'] = self.username 
        msgData['to'] = _to
        pickle.dump(msgData, open(str(int(self.msgConfig[msgBase]['totalMsgs']) + 1) + ".msg", "wb"))
        self.userConfig['msgbase'][msgBase]['numPosts'] = str(int(self.userConfig['msgbase'][msgBase]['lastRead']) + 1)
        self.updateUserConfig()
        self.msgConfig[msgBase]['totalMsgs'] = str(int(self.msgConfig[msgBase]['totalMsgs']) + 1)
        self.updateMsgConfig()

    def post(self, msgBase):
        _to = raw_input('to: ')
        _subject = raw_input('subject: ') 
        msg = []
        while(True):
            line = sys.stdin.readline()
            line = line.strip('\n')
            if line == '/s':
                self.saveMsg(msgBase, _to, _subject, msg)
                break
            msg.append(line+'\n')
 

    def reply(self, msgBase, msgNumber):
        pass

