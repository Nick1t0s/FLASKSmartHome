def checkPassword(request,credentials):
    data=request.form.to_dict()
    ip=request.remote_addr
    if data.get("password","1") == credentials.get(ip,"2"): return True
    return False