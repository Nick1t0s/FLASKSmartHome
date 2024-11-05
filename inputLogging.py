def getYn(message):
    res=input(message)
    while True:
        if res.lower() == "y": return True
        elif res.lower() == "n": return False