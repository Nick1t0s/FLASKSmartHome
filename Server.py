def createJsonCommands(request):
    args = request.args.to_dict()
    devicesDFSorted = devicesDF[devicesDF["id"] == args["id"]]
    commandsToExecute = devicesDFSorted["commandsToRun"][0]
    x={"commands":commandsToExecute.split()}
    xJS=json.dumps(x)
    return xJS

def createDeviceDir(request):
    pass

from flask import *
from flask import request
from flask import Flask
import json
import datetime
import pandas as pd
import logging
import os


app=Flask("Server.py")
# app.logger.disabled = True
# log = logging.getLogger('werkzeug')
# log.disabled = True
logging.basicConfig(level=logging.DEBUG)
devicesDF=pd.DataFrame({"id":[],
                        "ip":[],
                        "name":[],
                        "commands":[],
                        "cmDescription":[],
                        "dvDescription":[],
                        "lastConnection":[],
                        "commandsToRun":[]})
devicesCredentials=readDevices()
@app.route("/api/device/getCM/", methods=['GET'])
def deviceRequest():
    r = {'is_claimed': 'True', 'rating': 3.5}
    r = json.dumps(r)
    args = request.args.to_dict()
    if regDevice(request):
        writeDeviceToDF(request)
        answer=createJsonCommands(request)
    else:
        answer=json.dumps({"hello":"hello"})
    return answer

@app.route("/api/device/doneCommand/", methods=['GET','POST'])
def commandsPost():
    jsF=request.form.to_dict()
    print(jsF)
    return "asd"

@app.route("/api/device/writeData/",methods=["POST"])
def writeData():
    data=request.form.to_dict()
    password=data.get("password","wrondPS")
    ip=request.remote_addr
    fileName=data.get("fileName")
    if password==devicesCredentials.get(ip,"P"):
        if data.get("command","Err")=="writeFile":
            if fileName != "Err":
                file = request.files['file']
                file.save(os.path.join("gettedFiles",data.get("fileName")))
            else:
                logging.warning(f"Device by {ip} connected and tried to transfer the file, but the path was not specified")
        elif data.get("command","Err")=="writeDB"
    else:
        logging.warning(f"Device by {ip} tried to connect and transfer file, but password is wrong")
    return "ok"

@app.route("/api/device/SQL",methods=["POST"])
def SQL():
    data=request.form.to_dict()



if __name__== "__main__":
    app.run("0.0.0.0")
    logging.info("Started")