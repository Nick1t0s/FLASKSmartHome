import logging
import dt
def getLogFileName():
    return f"LogFile by{dt.getStrTimeNow(True)}.log"

def logConDevice(res, request, fileLoger, cmdLoger):
    data = request.form.to_dict()
    if res == "ok":
        fileLoger.info(f"Device connected ip: {request.remote_addr}, {data}")
        cmdLoger.info(f"Device connected ip: {request.remote_addr}, {data}")
    elif res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, " \
                        + f"wrong password: {data["password"]}")

def logLoadFile(res, request, fileLoger, cmdLoger)