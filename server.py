from shared_logic import timeout, run_forever
from shared_logic import *

from typing import Callable
import socket
import sys
import select
import logging

# better logging settings
logging.basicConfig(filename='serverLogFile.log', filemode='w', encoding='utf-8', level=logging.DEBUG)

TCP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp server
TCP_SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same port for multiple servers
TCP_SERVER.bind((IP, PORT)) # 127.0.0.1:4545
TCP_SERVER.listen() # set to listen mode
TCP_SERVER.setblocking(0)

SERVER_COMMANDS: dict[str, Callable] = {
    "@help": lambda: print(f">> List of commands: \n{' '.join(list(SERVER_COMMANDS))}")
}
logging.info("Server has been initialized")


@run_forever
def client_connection(**kwargs) -> bool:
    """This handles a client -> sending cmds to the client."""

    client, addr = kwargs['client'], kwargs['addr']

    cmd = input("> ")
    if cmd.startswith('@'):
        SERVER_COMMANDS.get(cmd, lambda: print(f"Could not find {cmd}"))()
        return True

    timeout(client, lambda _conn: _conn.send(cmd.encode(FORMAT)), None)

    connect_msg = timeout(client, lambda _client: _client.recv(1024).decode(FORMAT))
    print("[CLIENT]", connect_msg)
    return False


@run_forever
def handle_new_connection() -> None:
    """This handles new connections made to the server."""

    logging.debug("[Waiting] Handling new Connection started.")
    conn, addr = timeout(TCP_SERVER, lambda _conn: _conn.accept(), None)
    logging.info(f"New connection from {addr}")

    connect_msg = timeout(conn, lambda _conn: _conn.recv(8).decode(FORMAT), 5)
    logging.debug(f"Connection message received: {connect_msg}")
    if connect_msg == CONNECT_MSG:
        try:
            logging.debug("Sending confirm message.")
            timeout(conn, lambda _conn: _conn.send(CONNECT_MSG_REPLY.encode(FORMAT)), None)
            logging.debug(f"Starting communication with {addr}")
            client_connection(client=conn, addr=addr)
        except ConnectionTimeout as e:
            logging.warning(f"{addr} is not responding. {e}")
        except Exception as e:
            logging.warning(e)


if __name__ == '__main__':
    handle_new_connection()
