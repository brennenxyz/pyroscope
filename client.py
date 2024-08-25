import os
import asyncio
import websockets
from dotenv import load_dotenv

IP = os.getenv('IP')
PORT = os.getenv('PORT')

async def listen():
    uri = "ws://" + IP + ":" + PORT 
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

if __name__ == "__main__":
    asyncio.run(listen())