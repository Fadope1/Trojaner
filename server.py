import socket
import time


FORMAT = "utf-8"
PORT = 4545

BROADCASTER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp connection
BROADCASTER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same ports multiple servers
BROADCASTER.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # activate broadcasting

SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # same ports multiple servers
SERVER.bind(("", PORT))


def main():
    while True:
        data, addr = SERVER.recvfrom(8)
        print(str(data))
        msg = input("> ")
        if msg == 'close_all':
            BROADCASTER.sendto(msg, ('<broadcast>', PORT)) # broadcast on specified port
            break
        SERVER.sendto(bytes(msg, FORMAT), addr)


if __name__ == '__main__':
    main()
