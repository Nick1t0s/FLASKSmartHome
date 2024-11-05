import os
import sql
import logging
import sys
import inputLogging
def createDir(ip):
    if not os.path.exists("devices"): os.mkdir("devices")
    if not os.path.exists(f"devices\\{ip.replace(".","_")}"): os.mkdir(f"devices\\{ip.replace(".","_")}")
def createDIRTABLE(ip):
    createDir(ip)
    sql.createTable({"d1":"INTAGER","d2":"INTAGER"},ip)

def readCredentials(file):
    print(file)
    if os.path.exists(file):
        devicesCredentials={}
        with open(file) as file:
            counter=0
            for line in file:
                if line.count(" ")==1:
                    ip,password=line.split(" ")
                    devicesCredentials[ip]=password
                else:
                    if inputLogging.getYn(f"Y/n"):
                        logging.warning(f"Line {counter} does not match the format: {line}")
                        logging.warning(f"String missed")
                    else:
                        logging.error(f"Line {counter} does not match the format: {line}")
                        logging.error(f"Program stopped")
                        sys.exit(1)
        return devicesCredentials
    else:
        logging.error(f"No file settings, path: {file}")
        sys.exit(1)

sql.deleteTable("192.168.1.33")