import logging
import dt
def getLogFileName():
    return f"LogFile by{dt.getStrTimeNow(True)}.log"

def logConDevice(res, request):
    data = request.form.to_dict()
    if res == "ok":
        logging.info(f"Device connected by ip: {request.remote_addr}, {data}")
    elif res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, " \
                        + f"wrong password: {data["password"]}")

def logLoadFile(res, request,fullpath):
    data = request.form.to_dict()
    if res == "ok":
        logging.info(f"Device connected by ip: {request.remote_addr}, and write file by name: {fullpath}")
    if res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, " \
                        + f"wrong password: {data["password"]}")
def logGetFile(res,request,fullpath):
    data = request.form.to_dict()
    if res == "ok":
        logging.info(f"Device connected by ip: {request.remote_addr}, and get file by name: {fullpath}")
    elif res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, " \
                        + f"wrong password: {data["password"]}")
    elif res == "noFile":
        logging.info(f"Device connected by ip: {request.remote_addr}, and tried get file by name: {fullpath}, no file")