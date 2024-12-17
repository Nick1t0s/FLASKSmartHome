import sql


def createJsonCommands(request):
    args = json.loads(request.json)
    devicesDFSorted = devicesDF[devicesDF["id"] == args["id"]]
    if devicesDFSorted.shape[0]==0:
        commandsToExecute = ""
    else:
        commandsToExecute = devicesDFSorted["commandsToRun"][0]
    x={"commands":commandsToExecute.split()}
    xJS=json.dumps(x)
    print(devicesDF)
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
@app.route("/api/device/getCM/", methods=['POST'])
def deviceRequest():  # Функция ответа на запрос получения команд
    if security.checkPassword(request,devicesCredentials):
        controlDevices.writeDevice(devicesDF,request)
        answer=createJsonCommands(request)
    else:
        answer=json.dumps({"hello":"hello"})
    return answer

@app.route("/api/device/doneCommand/", methods=['GET','POST'])
def commandsPost():  # Функция регистрации выполнения команды
    jsF=request.form.to_dict()
    print(jsF)
    return "asd"

@app.route("/api/device/sendFile/",methods=["POST"])
def writeData():  # Прием файла
    return toolsRequest.downloadFile(request,devicesCredentials)

@app.route("/api/device/getFile/",methods=["POST"])
def getData():  # Отправка файла
    return toolsRequest.getFile(request,devicesCredentials)

@app.route("/api/device/SQL/",methods=["POST"])
def SQL():  # Выполнение SQL запроса
    return toolsRequest.useSQL(request,devicesCredentials)

@app.route("/api/user/SQL/",methods=["POST"])
def getCMDS():
    return toolsRequest.getCOMMANDS(request,usersCredentials,devicesDF)

if __name__== "__main__":
    app.run("0.0.0.0")
    logging.info("Started")