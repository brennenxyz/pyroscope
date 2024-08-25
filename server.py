# server.py
import os
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv()

IP = os.getenv('IP')
PORT = os.getenv('PORT')
clients = set() 

async def handle_connection(websocket, path):
    clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)

async def send_message(message):
    if clients:
        await asyncio.wait([client.send(message) for client in clients])
    else:
        print("No connected clients to send the message to.")

async def main():
    server = await websockets.serve(handle_connection, IP, int(PORT), ssl=None)
    print(f"WebSocket Secure Server running on ws://{IP}:{PORT}")
    await server.wait_closed()

if __name__ == "__main__":
    server_task = asyncio.ensure_future(main())

    try:
        while True:
            user_message = input("Enter a message to send to all clients: ")
            asyncio.run(send_message(user_message))
    except KeyboardInterrupt:
        print("Server shutting down...")
