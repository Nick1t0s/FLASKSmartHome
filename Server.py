import sys


def checkDevice(args):
    if "id" in args and "name" in args and "commands" in args \
    and "cmDescription" in args and "dvDescription" in args and "password" in args:
        return True
    return False
def getStrTimeNow(isStr):
    if isStr: return datetime.datetime.now().strftime("%d.%m.%Y %H %M %S")
    else: datetime.datetime.now()# .strftime("%d.%m.%Y %H:%M:%S")

def getLofFileName():
    return f"Logfile by{getStrTimeNow(True)}.log"

def checkLine(line):
    if line.count(" ") == 1: return True
    else: return False

def getYn(message):
    res=input(message)
    while True:
        if res.lower() == "y": return True
        elif res.lower() == "n": return False


def readDevices(path="devices.txt"):
    if os.path.exists(path):
        devicesCredentials={}
        with open(path) as file:
            counter=0
            for line in file:
                if checkLine(line):
                    ip,password=line.split(" ")
                    devicesCredentials[ip]=password
                else:
                    if getYn(f"Y/n"):
                        logging.warning(f"Line {counter} does not match the format: {line}")
                        logging.warning(f"String missed")
                    else:
                        logging.error(f"Line {counter} does not match the format: {line}")
                        logging.error(f"Program stopped")
                        sys.exit(1)
        return devicesCredentials

    else:
        if path=="devices.txt": logging.error(f"No file settings, base path: {path}")
        else: logging.error(f"No file settings, path: {path}")
        sys.exit(1)

def checkMessageCredentials(request,devicesCredentials):
    ip=request.remote_addr
    if request.args.to_dict().get("password","notP")==devicesCredentials.get(ip,"P"): return True
    else: return False

def regDevice(request):
    args=request.args.to_dict()
    if checkDevice(args):
        if checkMessageCredentials(request,devicesCredentials):
            logging.info(f"Device connected ip: {request.remote_addr}, {args}")
            return True
        else:
            logging.warning(f"Device tried to connect by ip: {request.remote_addr}, "\
            +f"wrong password: {args.get("password")}")
            return False
    else:
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, wrong arguments {args}")

def writeDeviceToDF(request):
    args=request.args.to_dict()
    devicesDFSorted=devicesDF[devicesDF["id"]==args["id"]]
    commandsToExecute=devicesDFSorted["commandsToRun"]
    devicesDF.loc[devicesDF.shape[0]] = [args["id"], request.remote_addr, args["name"], args["commands"],
                                         args["cmDescription"],args["dvDescription"],getStrTimeNow(False),
                                         ",".join(commandsToExecute)]

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