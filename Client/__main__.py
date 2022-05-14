import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # for testing only

client.bind(("", 5050))

client.sendto(b'#Connect', ("localhost", 4545))

while True:
    data = client.recv(1024)
    print(str(data))
    if data == b"#Close":
        break
