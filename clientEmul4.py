import json
import requests
file = {"file": (open('xxx.jpg', 'rb'), 'test.txt'), "data": json.dumps({"id":"0", "password":"ghtje"})}
res=requests.post("http://192.168.1.42:5000/api/device/sendFile/",files=file)
# with open("xxx.jpg","wb") as file:
#     file.write(res.con)
print(res.text)