import security
import files
import dt
import os
import log
import sql
from flask import send_file
import json

def downloadFile(request):
    data = request.form.to_dict()
    files.createDir(data["id"])  # Создаем директорию, если ее нет
    extension = data.get("extension","txt")
    fullPath = data.get("filename","noName")+f" by {dt.getStrTimeNow(True).replace(":"," ")}.{extension}"
    file = request.files['file']
    print(f"devices\\{data["id"]}\\{fullPath}")
    file.save(f"devices\\{data["id"]}\\{fullPath}")
    log.logLoadFile("ok",request,fullPath)
    return {"hello":"ok"}

def getFile(dic):
    file=dic["filename"]
    if os.path.exists(f"devices\\{dic["id"]}\\{file}"):
        log.logGetFile("ok",dic,file)
        print("OOOOOOOOOOOOOO")
        return send_file(f"devices\\{dic["id"]}\\{file}")
    else:
        log.logGetFile("noFile", dic, file)
        print("KKKKKKKKKKKKKKKKK")
        return {"hello":"nofile"}
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