from typing import Callable
import asyncio
import subprocess

import socket

PORT = 4545
FORMAT = "utf-8"

TCP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp server
TCP_SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same port for multiple servers
TCP_SERVER.bind(("localhost", PORT)) # 127.0.0.1:4545
TCP_SERVER.listen(1) # set to listen mode with max 1 connection

SERVER_COMMANDS: dict[str, Callable] = {
    "@help": lambda: print(f">> List of commands: \n{' '.join(list(SERVER_COMMANDS))}")
}


def run_forever(func, **kwargs):
    def inner(**kwargs):
        while True:
            func(**kwargs)
    return inner


@run_forever
def client_connection(**kwargs):
    client, addr = kwargs['client'], kwargs['addr']

    # ip, port = addr

    cmd = input("> ")
    if cmd in SERVER_COMMANDS:
        SERVER_COMMANDS.get(cmd)()
        return

    client.send(cmd.encode(FORMAT))

    connect_msg = client.recv(1024).decode(FORMAT)
    print(connect_msg)


@run_forever
def handle_new_connection():
    conn, addr = TCP_SERVER.accept()

    with conn as client:
        connect_msg = client.recv(8).decode(FORMAT)
        if connect_msg == "#Connect":
            client_connection(client=client, addr=addr)


if __name__ == '__main__':
    handle_new_connection()
