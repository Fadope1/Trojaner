from threading import Thread
import socket
import sys


ADDR = socket.gethostbyname(socket.gethostname()) # local ip address
PORT = 4545
SOCKET = (ADDR, PORT)
FORMAT = "utf-8"
CLOSE_TAG = "#Close"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a udp server over ip
server.bind(SOCKET) # bind server to our addr + port

clients = set()


def handle_new_connections():
    while True:
        msg, addr = server.recvfrom(8)
        print(msg)
        clients.add(addr)


def broadcast():
    global clients
    
    while True:
        msg = input("")
        if msg == "#exit":
            sys.exit()
        print(clients)
        for client in clients:
            server.sendto(bytes(msg, FORMAT), client)
        if msg == CLOSE_TAG:
            clients = set()


if __name__ == '__main__':
    Thread(target = handle_new_connections).start()
    Thread(target = broadcast).start()
