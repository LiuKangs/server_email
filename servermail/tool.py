
from time import sleep
from imap_tools import MailBox, AND
import asyncio
import websockets
import json

async def send_mail(mess):
    async with websockets.connect("ws://localhost:1000") as websocket:
        data = {'who':'tool',
                'info': 'tool',
                'mail':json.loads(mess)}
        await websocket.send(json.dumps(data))
        print('đã có mail mới !')

async def Mail():
    imap_host = 'mail.maxbulon.com'
    imap_user = '_mainaccount@maxbulon.com'
    imap_pass = 'Nguyenhoanganh2004@'
    while True :
        with MailBox(imap_host).login(imap_user, imap_pass, 'INBOX') as mailbox:
            fec = mailbox.fetch(AND(seen=False))
            for msg in fec:
                r = {
                    "from" : msg.from_ ,
                    "to" : msg.to ,
                    "body" : msg.text ,
                    'header' : msg.headers ,   
                }   
                await send_mail(json.dumps(r))             
                print('đã gởi mail mới tới server!')
        sleep(2)

asyncio.run(Mail())