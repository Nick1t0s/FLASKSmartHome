import json
import requests
file = {"file": open('xxx.jpg', 'rb')}
data = {"id":"0", "password":"ghtje", "filename": "test.jpg", "extension":"jpg"}
res=requests.post("http://192.168.1.42:5000/api/device/sendFile/",files=file, data=data)
# with open("xxx.jpg","wb") as file:
#     file.write(res.con)
print(res.text)
if res.status_code =