import json
def checkPassword(dic,credentials):
    if dic.get("password","1") == credentials.get(dic.get("id"),"2"): return True
    return False
