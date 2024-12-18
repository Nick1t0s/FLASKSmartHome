import json
import requests
data = {"id":"0", "password":"ghtje", "filename": "test.jpg by 18.12.2024 16 30 36.jpg"}
data = {"id":"0","password":"ghtje", "filename": "test.jpg by 18.12.2024 16 30 36.jpg"}
res=requests.post("http://192.168.1.42:5000/api/device/getFile/",json=json.dumps(data))
with open("dd.jpg","wb") as file:
    file.write(res.content)
