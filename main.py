import websockets
import asyncio

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com') as socket:
        message = await socket.recv()
        print(message)
            
asyncio.run(start())