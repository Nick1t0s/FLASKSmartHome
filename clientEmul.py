import json
import requests
msg = "Твой текст!"
with open("scale_1200.jpg","rb") as file:
    file={"file":file.read()}
data = {"command": "writeFile","path":"d.jpg","password":"ghtje","fileName":"scale_1200","extension":"jpg"}
res=requests.post("http://192.168.1.42:5000/api/device/sendFile/",data=data,files=file)
print(res.status_code)