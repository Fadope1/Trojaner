import socket
import threading
from multiprocessing import Process


ADDR = socket.gethostbyname(socket.gethostname()) # local ip address
PORT = 4545
SOCKET = (ADDR, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a udp server over ip
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.bind(SOCKET) # bind server to our addr + port

clients = set()

# TODO: Add threading for handling connection and broadcasting
# multiprocessing and logging
# handle end of connection


def handle_new_connections():
    print("nice2")
    # while True:
    #     msg, addr = server.recvfrom(8)
    #     print(msg)
    #     clients.add(addr)


def broadcast():
    print("nice")
    # msg = input("> ")
    # print(clients)
    # for client in clients:
    #     server.sendto(binary(msg, FORMAT))


p1 = Process(target = lambda x: print(x))
p2 = Process(target = broadcast)
p1.start()
p2.start()
p1.join()
p2.join()
