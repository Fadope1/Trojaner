import asyncio
import sys

import websockets

# Why is async used here?


async def hello():
    async with websockets.connect("ws://localhost:4545") as websocket:
        await websocket.send(str(sys.argv[1])) # replace by id
        print(await websocket.recv())


asyncio.run(hello())
