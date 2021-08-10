import websockets
import asyncio

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com') as socket:
            while True:
                message = await socket.recv()
                print(message)
                
                asyncio.sleep(60)
                
asyncio.run(start())