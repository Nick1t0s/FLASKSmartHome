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
    print(json.loads(request.json))
    if security.checkPassword(json.loads(request.json),devicesCredentials):
        controlDevices.writeDevice(devicesDF,json.loads(request.json))
        answer=createJsonCommands(request)
    else:
        answer=json.dumps({"hello":"hello"})
    # print(devicesDF)
    return answer

@app.route("/api/device/doneCommand/", methods=['GET','POST'])
def commandsPost():  # Функция регистрации выполнения команды
    jsF=request.form.to_dict()
    # print(jsF)
    return "asd"

@app.route("/api/device/sendFile/",methods=["POST"])
def writeData():  # Прием файла
    if security.checkPassword(request.form.to_dict(), devicesCredentials):
        return toolsRequest.downloadFile(request)
    else:
        return json.dumps({"hello":"hello"})

@app.route("/api/device/getFile/",methods=["POST"])
def getData():  # Отправка файла
    print(json.loads(request.json))
    print(devicesCredentials)
    if security.checkPassword(json.loads(request.json), devicesCredentials):
        return toolsRequest.getFile(json.loads(request.json))
    else:
        return {"hello":"hello"}

@app.route("/api/device/SQL/",methods=["POST"])
def SQL():  # Выполнение SQL запроса
    return toolsRequest.useSQL(request,devicesCredentials)

@app.route("/api/user/getDevices/",methods=["POST"])
def getDevices():
    if security.checkPassword(json.loads(request.json),usersCredentials):
        answer = devicesDF.to_dict()
        for i in answer:
            answer[i] = list(answer[i].values())
    else:
        answer = {"hello":"hello"}
    return json.dumps(answer)

@app.route("/api/user/writeCMD/", methods=["POST"])
def writeCMD():
    if security.checkPassword(json.loads(request.json),usersCredentials):
        answer = controlDevices.writeCommand(devicesDF, json.loads(request.json))
    else:
        answer = {"hello":"hello"}
    return json.dumps(answer)

@app.route("/api/user/SQL/", methods=["POST"])
def getCMDS():
    return toolsRequest.getCOMMANDS(request,usersCredentials,devicesDF)

if __name__== "__main__":
    app.run("0.0.0.0")
    logging.info("Started")