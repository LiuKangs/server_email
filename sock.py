


'''
projcet này tạo 1 server nhận mail code

server sẽ lắng nghe mail đến để phân loại gởi về cho client

'''

from time import sleep
from imap_tools import MailBox, AND
import asyncio

import json



CONNECTER = {}




async def getMailCode():
    '''
    hàm ``getMailCode()`` dùng để lấy về đối tượng mail chưa đọc
    
    (mail : mail cần lấy code)
    
    - Dữ liệu trả về là opcode hoặc None
    - Nếu không tìm thấy tin nhắn mới sẽ trả về None
    '''
    imap_host = 'mail.maxbulon.com'
    imap_user = '_mainaccount@maxbulon.com'
    imap_pass = 'Nguyenhoanganh2004@'


    while True :
        with MailBox(imap_host).login(imap_user, imap_pass, 'INBOX') as mailbox:
            fec = mailbox.fetch(AND(seen=False))
            for msg in fec:
            # for msg in mailbox.fetch(from)    
                body = msg.text
                print(msg.from_)
                # if body.find(mail) != -1:
                #     otp_code = findOtpCode(body)
                #     if otp_code != None:
                #         return otp_code[0]
                #     break
        sleep(2)
        

import websockets

async def hello(mess):
    async with websockets.connect("ws://127.0.0.1:11") as websocket:
        data = {'tool':'tool',
                'mess':mess}
        await websocket.send(json.dumps(data))
        print('đã send mail mới tới server')

async def Mail():
    imap_host = 'mail.maxbulon.com'
    imap_user = '_mainaccount@maxbulon.com'
    imap_pass = 'Nguyenhoanganh2004@'
    while True :
        with MailBox(imap_host).login(imap_user, imap_pass, 'INBOX') as mailbox:
            fec = mailbox.fetch(AND(seen=False))
            for msg in fec:
            # for msg in mailbox.fetch(from)    
                await hello(msg.from_)
                
                print(msg.from_)
                # if body.find(mail) != -1:
                #     otp_code = findOtpCode(body)
                #     if otp_code != None:
                #         return otp_code[0]
                #     break
        sleep(2)



async def handler(websocket):
    """
    Handle a connection and dispatch it according to who is connecting.

    """
    global CONNECTER
    message = await websocket.recv()
    try:
        message = json.loads(message)
        print(message)
        if message.get('tool') ==  None :
            CONNECTER.add(websocket)
            try:
                print(CONNECTER)
            finally:
                CONNECTER.remove(websocket)
    except:
        ...
    
    # event = json.loads(message)
    # assert event["type"] == "init"

    # if "join" in event:
    #     # Second player joins an existing game.
    #     await join(websocket, event["join"])
    # elif "watch" in event:
    #     # Spectator watches an existing game.
    #     await watch(websocket, event["watch"])
    # else:
    #     # First player starts a new game.
    #     await start(websocket)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 11):
        await asyncio.Future()  # run forever
async def start():
    await asyncio.gather(main(),Mail())
asyncio.run(start())
             

        