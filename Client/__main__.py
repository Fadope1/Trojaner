import socket


SERVER_ADDR = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 4545
ADDR = (SERVER_ADDR, SERVER_PORT)

FORMAT = 'utf-8'
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# msg = CLIENT.recv(1024).decode(FORMAT)
CLIENT.sendto(bytes("#Connect", FORMAT), ADDR)

msg = None
while msg != "#Close":
    msg = str(CLIENT.recvfrom(8)[0], FORMAT)
    print(msg)
