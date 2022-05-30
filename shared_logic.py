import select
import time
import socket
import errno

###### GLOBAL VARS ######
IP = "localhost"
PORT = 4545

FORMAT = "utf-8"

TIMEOUT = 10 # seconds before failure
#########################

###### MESSAGES #########
CONNECT_MSG = "#Connect"
CONNECT_MSG_REPLY = "#Connect_confirm"

EMPTY_MSG = "#Empty_run"
#########################


class ConnectionTimeout(Exception):
    """Raised when connection has as timeout."""


def timeout(conn, func, timeout_time=TIMEOUT):
    """send msg.bytes with timeout."""
    if not timeout_time:
        while True:
            try:
                msg = func(conn)
            except socket.error as e:
                err = e.args[0]
                if err != errno.EAGAIN or err != errno.EWOULDBLOCK:
                    raise ConnectionTimeout("Connection has timed out")
            else:
                return msg

    ready = select.select([conn], [], [], TIMEOUT) # wait for ready for reading, wait 10 sec for confirm
    if ready[0]:
        return func(conn)
    raise ConnectionTimeout("Connection has timed out")
