import datetime
def getStrTimeNow(isStr):
    if isStr: return datetime.datetime.now().strftime("%d.%m.%Y %H %M %S")
    else: datetime.datetime.now()# .strftime("%d.%m.%Y %H:%M:%S")