import websockets
import asyncio
from datetime import datetime

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com', ping_interval = None) as socket:
        while True:
            await socket.send(f'{datetime.now().timestamp()},["admin","init",[0,3,2390],["Long browser description","ShortBrowserDesc"],"enbekeksuenb",true]')
            print(await socket.recv())
            await asyncio.sleep(10)
        
asyncio.run(start())