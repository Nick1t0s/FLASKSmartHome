import security
import files
import dt
import os
import log
def downloadFile(request,devicesCredentials):
    data = request.form.to_dict()
    if security.checkPassword(request,devicesCredentials):
        files.createDir(request.remote_addr)
        ip = request.remote_addr
        extension = data.get("extension","")
        fullPath = data.get("fileName","noName")+f" by {dt.getStrTimeNow(True)}.{extension}"
        file = request.files['file']
        file.save(f"devices\\{ip.replace(".","_")}\\{fullPath}")
        log.logLoadFile("ok",request,fullPath)
    else:
        log.logLoadFile("wrongPass",request,"")

def get