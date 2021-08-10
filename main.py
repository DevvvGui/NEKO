import websockets
import asyncio

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com') as socket:
        await socket.send('emgejsks,["admin","init",[0,3,2390],["Long browser description","ShortBrowserDesc"],"enbekeksuenb",true]')
        message = await socket.recv()
        print(message)
        
asyncio.run(start())