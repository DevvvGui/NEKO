import websockets
import asyncio

runnings = 0

async def start():
    global runnings
    
    async with websockets.connect('wss://web.whatsapp.com/ws', origin = 'https://web.whatsapp.com', ping_interval = None) as socket:
        while True:
            runnings += 1
            
            await socket.send(f'running-{runnings},["admin","init",[0,3,2390],["Long browser description","ShortBrowserDesc"],"enbekeksuenb",true]')
            message = await socket.recv()
            print(message)
        
            await asyncio.sleep(10)
        
asyncio.run(start())