from multiprocessing import Process
import asyncio

import websockets

"""
1. Have a handler that connects a new connection to a list
2. wait for user input
3. send user input to ALL connections in list
"""

connections = {}


def handle_new_connections():
    async def handler(websocket):
        async for message in websocket:
            connections[message] = websocket
            # await websocket.send(message)

    async def main():
        async with serve(echo, "localhost", 4545):
            await asyncio.Future()  # run forever

    asyncio.run(main())


def reverse_shell():
    while True:
        print(connections)


send_comands = Process(target=reverse_shell)
get_new_connections = Process(target=handle_new_connections)
get_new_connections.start()
send_comands.start()
