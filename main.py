import websockets
import asyncio

async def start():
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com') as socket:
            while True:
                print(socket.messages.pop())
                
asyncio.run(start())