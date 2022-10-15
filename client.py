
import asyncio , json
import websockets


from websocket import create_connection

ws = create_connection("ws://127.0.0.1:11")
data = {
                'mess':''}
ws.send(json.dumps(data))
print(ws.recv())

