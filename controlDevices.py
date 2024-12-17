import pandas as pd
import dt
import json
def getDF():
    devicesDF=pd.DataFrame({"id": [],
                              "ip": [],
                              "name": [],
                              "commands": [],
                              "cmDescription": [],
                              "dvDescription": [],
                              "lastConnection": [],
                              "commandsToRun": []})
    return devicesDF

def writeDevice(devicesDF,request):
    data=json.loads(request.json)
    print(data)
    devicesDFSorted=devicesDF[devicesDF["id"]==data["id"]]
    commandsToExecute=devicesDFSorted["commandsToRun"]
    listForWrite=[data["id"], request.remote_addr, data["name"],
                  ",".join(data["commands"]) if type(data["commands"]) == list else data["commands"],
                  ",".join(data["cmDescription"]) if type(data["cmDescription"]) == list else data["cmDescription"],
                  ""
                  dt.getStrTimeNow(True),
                  "sdf","sdf","sdfgf"]
    print(listForWrite)
    devicesDF.loc[devicesDF.shape[0]] = listForWrite
    return devicesDF
