
# hàm nhận mail từ client   

import json
from websocket import create_connection

ws = create_connection("ws://localhost:1000")
print("wait lisening server ! ")
# 1 : chuyển hướng mail google
# 2 : 
dataStart = {
    "who" : '' ,
    "service" : "1" ,
    "info" : {
        'mail' : "phatkervn1@gmail.com"
    } 
}

ws.send(json.dumps(dataStart))
result =  ws.recv()
print("Received '%s'" % result)
ws.close()