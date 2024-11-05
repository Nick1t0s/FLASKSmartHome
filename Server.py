

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
import files
import toolsRequest
import security
import controlDevices


app=Flask("Server.py")
# app.logger.disabled = True
# log = logging.getLogger('werkzeug')
# log.disabled = True
logging.basicConfig(level=logging.DEBUG) #log.getLogFileName()
devicesDF=controlDevices.getDF()
devicesCredentials=files.readCredentials("credentials\\devices.txt")
usersCredentials=files.readCredentials("credentials\\users.txt")
rootsCredentials=files.readCredentials("credentials\\roots.txt")
@app.route("/api/device/getCM/", methods=['GET'])
def deviceRequest():
    r = {'is_claimed': 'True', 'rating': 3.5}
    r = json.dumps(r)
    args = request.args.to_dict()
    if security.checkPassword(request):
        controlDevices.writeDevice(devicesDF,request)
        answer=createJsonCommands(request)
    else:
        answer=json.dumps({"hello":"hello"})
    return answer

@app.route("/api/device/doneCommand/", methods=['GET','POST'])
def commandsPost():
    jsF=request.form.to_dict()
    print(jsF)
    return "asd"

@app.route("/api/device/sendFile/",methods=["POST"])
def writeData():
    toolsRequest.downloadFile(request,devicesCredentials)
    return "ok"

@app.route("/api/device/getFile",methods=["POST"])
def writeData():


@app.route("/api/device/SQL",methods=["POST"])
def SQL():
    data=request.form.to_dict()



if __name__== "__main__":
    app.run("0.0.0.0")
    logging.info("Started")