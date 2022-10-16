

import asyncio
import websockets
import json


async def send_mail(mess):
    async with websockets.connect("ws://localhost:1000") as websocket:
        dataStart = {
            "who": 'tool',
            "mail":{
                "from" : "google.com",
                "body" : "hello",
                "header" : "hello"
            }
        }
        await websocket.send(json.dumps(dataStart))
        print('đã gởi mail mới tới server!')

asyncio.run(send_mail('hdshkfk'))
