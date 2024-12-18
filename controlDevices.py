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
    data = json.loads(request.json)
    devicesDFSorted = devicesDF[devicesDF["id"]==data["id"]]
    commandsToExecute = devicesDFSorted["commandsToRun"].tolist()
    if commandsToExecute == []:
        commandsToExecute = ""
    else:
        commandsToExecute = ",".join(commandsToExecute[0])
    # print(commandsToExecute)
    listForWrite=[data["id"], request.remote_addr, data["name"],  # ID, IP, NAME
                  ",".join(data["commands"]) if type(data["commands"]) == list else data["commands"],  # Commands
                  ",".join(data["cmDescription"]) if type(data["cmDescription"]) == list else data["cmDescription"],
                  data["dvDescription"], dt.getStrTimeNow(True),
                  commandsToExecute]
    if len(devicesDFSorted) == 0:
        # print(listForWrite)
        devicesDF.loc[devicesDF.shape[0]] = listForWrite
    else:
        devicesDF.loc[devicesDF["id"] == data["id"]] = listForWrite
    return devicesDF

def writeCommand(devicesDF,request):
    data = json.loads(request.json)
    ids = devicesDF['id'].tolist()
    idDev = data.get("idDev", "nid")
    if idDev in ids:
        new_val = devicesDF.loc[devicesDF['id'] == idDev].iloc[0].to_list()
        new_val[7] = ",".join(new_val[7].split(",")+data["command"]).strip(",")
        print(new_val)
        devicesDF.loc[devicesDF["id"] == idDev] = new_val
        return {"hello": "ok"}
    else:
        return {"hello":"noID"}

