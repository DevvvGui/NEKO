import websockets
import asyncio
from datetime import datetime

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com', ping_interval = None) as socket:
        while True:
            timestamp = int(datetime.now().timestamp())
            
            await socket.send(f'{timestamp},["admin","init",[0,3,2390],["Long browser description","ShortBrowserDesc"],"{timestamp}",true]')
            print(await socket.recv())
            await asyncio.sleep(1)
            
asyncio.run(start())