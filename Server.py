import sqlite3


def createJsonCommands(request):
    args = json.loads(request.json)
    devicesDFSorted = devicesDF[devicesDF["id"] == args["id"]]
    if devicesDFSorted.shape[0]==0:
        commandsToExecute = ""
    else:
        commandsToExecute = devicesDFSorted["commandsToRun"].to_list()
        print(commandsToExecute)
    x={"commands":commandsToExecute}
    xJS=json.dumps(x)
    # print(devicesDF)
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
    print(devicesDF)
    return answer

@app.route("/api/device/doneCommand/", methods=['GET','POST'])
def commandsPost():  # Функция регистрации выполнения команды
    jsF=request.form.to_dict()
    # print(jsF)
    return "asd"

@app.route("/api/device/sendFile/",methods=["POST"])
def writeData():  # Прием файла
    # if security.checkPassword(request, devicesCredentials):
    #     return json.dumps({"h":"h"})
    # else:
    print(request.form)
    return json.dumps({"hello":"hello"})

@app.route("/api/device/getFile/",methods=["POST"])
def getData():  # Отправка файла
    return toolsRequest.getFile(request,devicesCredentials)

@app.route("/api/device/SQL/",methods=["POST"])
def SQL():  # Выполнение SQL запроса
    return toolsRequest.useSQL(request,devicesCredentials)

@app.route("/api/user/getDevices/",methods=["POST"])
def getDevices():
    if security.checkPassword(request,usersCredentials):
        # controlDevices.writeDevice(devicesDF,request)
        # answer=createJsonCommands(request)
        # print(devicesDF.to_dict())
        answer = devicesDF.to_dict()
        for i in answer:
            answer[i] = list(answer[i].values())
        # print(answer)
    else:
        answer = {"hello":"hello"}
    return json.dumps(answer)

@app.route("/api/user/writeCMD/", methods=["POST"])
def writeCMD():
    if security.checkPassword(request, usersCredentials):
        answer = controlDevices.writeCommand(devicesDF, request)
    else:
        answer = {"hello":"hello"}
    return json.dumps(answer)

@app.route("/api/user/SQL/", methods=["POST"])
def getCMDS():
    return toolsRequest.getCOMMANDS(request,usersCredentials,devicesDF)

if __name__== "__main__":
    app.run("0.0.0.0")
    logging.info("Started")