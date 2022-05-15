"""
All static Vars and config settings

Cipher Codes (Startswith):
# -> Client message to Server
? -> Server message to Client
@ -> Server instruction
"""

from Server.exceptions import AccessDenied, CloseServer

from typing import Callable

FORMAT = "utf-8"
PORT = 4545
SECRET_PASSWORD = "123" # how to store securly?


def validate_admin() -> bool:
    """Ask for admin password and validate -> 3 tries"""
    tries = 3
    for i in range(tries):
        secret_key =  input("Secret key: ")

        if secret_key == SECRET_PASSWORD:
            raise CloseServer()
    raise AccessDenied("wrong password")


ciphers: dict[str, Callable] = {
    "@StopServer": validate_admin,
    "@help": lambda: "Sry, not implemented yet"
}
