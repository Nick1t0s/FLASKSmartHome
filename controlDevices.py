import pandas as pd
import dt
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
    data=request.form.to_dict()
    devicesDFSorted=devicesDF[devicesDF["id"]==data["id"]]
    commandsToExecute=devicesDFSorted["commandsToRun"]
    devicesDF.loc[devicesDF.shape[0]] = [data["id"], request.remote_addr, data["name"], data["commands"],
                                         data["cmDescription"],data["dvDescription"],dt.getStrTimeNow(False),
                                         ",".join(commandsToExecute)]
    return devicesDF
