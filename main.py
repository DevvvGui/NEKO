import asyncio
import pyqrcode

from kyros import Client, WebsocketMessage

async def start():
    client = await Client.create()
    qrdata = await client.qr_login()
    qrcode = pyqrcode.create(qrdata)
    
    print(qrcode.terminal())
    
asyncio.run(start())
    