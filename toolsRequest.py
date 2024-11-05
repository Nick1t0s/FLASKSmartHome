import security
import files
import dt
import os
def downloadFile(request):
    data = request.form.to_dict()
    devicesCredentials = files.readCredentials("credentials\\devices.txt")
    if security.checkPassword(request,devicesCredentials):
        ip = request.remote_addr
        extension = data.get("extension","")
        fullPath = data.get("fileName","noName")+f" by {dt.getStrTimeNow(True)}.{extension}"
        file = request.files['file']
        file.save(f"devices\\{ip.replace(".","_")}\\{fullPath}")

