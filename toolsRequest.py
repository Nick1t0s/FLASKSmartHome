import security
import files
import dt
import os
import log
import sql
from flask import send_file
import json

def downloadFile(request,devicesCredentials):
    data = json.loads(request.json)
    if security.checkPassword(request,devicesCredentials):
        files.createDir(request.remote_addr)
        ip = request.remote_addr
        extension = data.get("extension","")
        fullPath = data.get("fileName","noName")+f" by {dt.getStrTimeNow(True)}.{extension}"
        file = request.files['file']
        file.save(f"devices\\{ip.replace(".","_")}\\{fullPath}")
        log.logLoadFile("ok",request,fullPath)
        return "ok"
    else:
        log.logLoadFile("wrongPass",request,"")
        return "wrong"

def getFile(request,devicesCredentials):
    data = json.loads(request.json)
    if security.checkPassword(request, devicesCredentials):
        files.createDir(request.remote_addr)
        ip = request.remote_addr
        file=data.get("fileName")
        if os.path.exists(f"devices\\{ip.replace(".","_")}\\{file}"):
            log.logGetFile("ok",request,file)
            return send_file(f"devices\\{ip.replace(".","_")}\\{file}")
        else:
            log.logGetFile("noFile", request, file)
            return "noFile"
    else:
        file = data.get("fileName","")
        log.logGetFile("wrongPass",request,file)
        return "wrong"

def useSQL(request,devicesCredentials):
    data = json.loads(request.json)
    print(data)
    if security.checkPassword(request, devicesCredentials):
        columns=data.get("columns","123")
        if columns == "123":
            return "wrong"
        else:
            sqlExec=data.get("sqlExec","")
            sql.createTable(columns,request.remote_addr)
            res=sql.execSQL(request.remote_addr,sqlExec)
            return res
    else:
        print()
        return "wrong"

def getCOMMANDS(request,usersCredentials,devicesDF):
    data = json.loads(request.json)
    if security.checkPassword(request, usersCredentials):
        s={ip:name for ip,name in zip(devicesDF["ip"],devicesDF["name"])}
        print(s)
    return "df"