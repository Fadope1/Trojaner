"""
All static Vars and config settings

Cipher Codes (Startswith):
# -> Client message to Server
? -> Server message to Client
@ -> Server instruction
"""

from typing import Callable
import logging

import coloredlogs

logging.basicConfig(filename="logfilename.log", level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='WARNING')

FORMAT = "utf-8"
PORT = 4545

commands: dict[str, Callable] = {
    "@stopserver": lambda: input(">> You sure? (y/n) ").lower() == "y",
    "@help": lambda: print(">> Hi :)")
}
