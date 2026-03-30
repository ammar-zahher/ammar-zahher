import urllib.request, urllib.parse, urllib.error
import json
url=" http://py4e-data.dr-chuck.net/comments_2188410.json"
print("Retrieving :",url)
socket=urllib.request.urlopen(url)
data=socket.read().decode()
retrieved_data=json.loads(data)
placeholder=0
for item in retrieved_data["comments"]:
    placeholder=placeholder+int(item["count"])
print(placeholder)
