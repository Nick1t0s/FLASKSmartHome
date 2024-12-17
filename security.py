import json
def checkPassword(request,credentials):
    data = json.loads(request.json)
    ip = request.remote_addr
    if data.get("password","1") == credentials.get(ip,"2"): return True
    return False
