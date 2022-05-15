"""All servers in use"""

from Server.config import PORT

import socket

# Broadcast Server
BROADCAST_SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp server
BROADCAST_SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same ports multiple servers
BROADCAST_SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # activate broadcasting

# Point 2 Point server
TCP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp server
TCP_SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same ports multiple servers
TCP_SERVER.bind(("", PORT))

SERVERS: dict[str, socket.socket] = {"broadcast": BROADCAST_SERVER, "p2p": TCP_SERVER}


def close_all_servers() -> bool:
    """close all servers"""
    for _, server in SERVERS.items():
        server.close()

    return True # exception handling


def close_server_by_name(server_name) -> bool:
    """close one server by key"""
    SERVERS[server_name].close()

    return True # exception handling
