"""
All static Vars and config settings

Cipher Codes (Startswith):
# -> Client message to Server
? -> Server message to Client
@ -> Server instruction
"""

from Server.exceptions import AccessDenied, CloseServer

from typing import Callable
import logging

import coloredlogs

logging.basicConfig(filename="logfilename.log", level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='WARNING')

TIMEOUT_TIME = 1 # seconds

FORMAT = "utf-8"
PORT = 4545
SECRET_PASSWORD = "123" # how to store securely?


def validate_admin() -> bool:
    """Ask for admin password and validate -> 3 tries"""
    tries = 3
    for i in range(tries):
        secret_key =  input("Secret key: ")

        if secret_key == SECRET_PASSWORD:
            raise CloseServer()
    raise AccessDenied("wrong password")


ciphers: dict[str, Callable] = {
    "@stopserver": validate_admin,
    "@help": lambda: print("hi")
}
