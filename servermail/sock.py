


'''
projcet này tạo 1 server nhận mail code

server sẽ lắng nghe mail đến để phân loại gởi về cho client

'''


from imap_tools import MailBox, AND
import asyncio
import websockets
import json



CONNECTER = set()

type1 = {}

async def handler(websocket):
    CONNECTER.add(websocket)
    try:
        while True:
            try:
                message =  await websocket.recv()
                data = json.loads(message)
                if data['who'] == 'tool':    
                    for connect in CONNECTER:
                        if connect != websocket :
                            # check kiểu rồi gởi cho client
                            await connect.send(json.dumps(data['mail']))
                    break
                else:
                    if data['service'] == '1':
                        from_ = data['info']['mail']
                        type1[websocket] = from_
                        print(type1)
            except websockets.ConnectionClosedOK:
                break
            except websockets.exceptions.ConnectionClosedError :
                break
            
    finally:
        #type1.pop(websocket)
        CONNECTER.remove(websocket)
        
    

async def main():
    async with websockets.serve(handler, "localhost", 1000):
        await asyncio.Future()  # run forever

asyncio.run(main())


        