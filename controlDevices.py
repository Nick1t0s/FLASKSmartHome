import pandas as pd
import dt
import json
def getDF():
    devicesDF=pd.DataFrame({"id": [],
                              "name": [],
                              "commands": [],
                              "cmDescription": [],
                              "dvDescription": [],
                              "lastConnection": [],
                              "commandsToRun": []})
    return devicesDF

def writeDevice(devicesDF,dic):
    devicesDFSorted = devicesDF[devicesDF["id"]==dic["id"]]
    print(devicesDFSorted["commandsToRun"].tolist())
    commandsToExecute = devicesDFSorted["commandsToRun"].tolist()
    if commandsToExecute == []:
        commandsToExecute = ""
    else:
        commandsToExecute = ",".join(commandsToExecute)
    # print(commandsToExecute)
    listForWrite=[dic["id"], dic["name"],  # ID, IP, NAME
                  ",".join(dic["commands"]) if type(dic["commands"]) == list else dic["commands"],  # Commands
                  ",".join(dic["cmDescription"]) if type(dic["cmDescription"]) == list else dic["cmDescription"],
                  dic["dvDescription"], dt.getStrTimeNow(True),
                  commandsToExecute]
    if len(devicesDFSorted) == 0:
        # print(listForWrite)
        devicesDF.loc[devicesDF.shape[0]] = listForWrite
    else:
        devicesDF.loc[devicesDF["id"] == dic["id"]] = listForWrite
    return devicesDF

def writeCommand(devicesDF,dic):
    ids = devicesDF['id'].tolist()
    idDev = dic.get("idDev", "nid")
    if idDev in ids:
        new_val = devicesDF.loc[devicesDF['id'] == idDev].iloc[0].to_list()
        new_val[6] = ",".join(new_val[6].split(",")+dic["command"]).strip(",")
        print(new_val)
        devicesDF.loc[devicesDF["id"] == idDev] = new_val
        return {"hello": "ok"}
    else:
        return {"hello":"noID"}

