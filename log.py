import logging
import dt
def getLogFileName():
    return f"LogFile by{dt.getStrTimeNow(True)}.log"

def logConDevice(res, dic):
    if res == "ok":
        logging.info(f"Device connected by id: {dic["id"]}, {dic}")
    elif res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {request.remote_addr}, " \
                        + f"wrong password: {dic["password"]}")

def logLoadFile(res, dic, fullpath):
    if res == "ok":
        logging.info(f"Device connected by ip: {dic["id"]}, and write file by name: {fullpath}")
    if res == "wrongPass":
        logging.warning(f"Device tried to connect by ip: {dic["id"]}, " \
                        + f"wrong password: {dic["password"]}")
def logGetFile(res,dic,fullpath):
    if res == "ok":
        logging.info(f"Device connected by id: {dic["id"]}, and get file by name: {fullpath}")
    elif res == "wrongPass":
        logging.warning(f"Device tried to connect by id: {dic["id"]}, " \
                        + f"wrong password: {dic["password"]}")
    elif res == "noFile":
        logging.info(f"Device connected by id: {dic["id"]}, and tried get file by name: {fullpath}, no file")