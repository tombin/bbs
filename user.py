def checkUserExists(username):
    userHash = {}
    with open("passwd", "r") as fd:
        for line in fd:
            line = line.strip('\n')
            (user, pw) = line.split(':')
            userHash[user] = 1
    if username in userHash.keys():
        return True 
    else:
        return False 



