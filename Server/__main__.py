import asyncio
import subprocess
import sys

import websockets

PORT = 4545


async def handler(websocket):
    while True:
        try:
            payload = input("> ")
            await websocket.send(str(payload))
        except Exception as e:
            print(e) # logging


start_server = websockets.serve(handler, port=PORT)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
