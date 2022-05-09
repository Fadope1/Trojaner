import asyncio

import websockets

HOST = "192.168.178.139"
PORT = 4545


def run_forever(func):
    async def inner():
        try:
            return await func()
        except Exception as e:
            print(e) # logging
    return inner


@run_forever
async def handler():
    async with websockets.connect(f'ws://{HOST}:{PORT}') as websocket:
        cmd = await websocket.recv()
        print(cmd)


asyncio.run(handler())
