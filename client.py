import socket

FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # for testing only

client.connect(("localhost", 4545))

client.send('#Connect'.encode(FORMAT))

while True:
    reply = client.recv(1024).decode(FORMAT)
    print(reply)

    client.send(reply.encode(FORMAT))
    # reply = subprocess.run(cmd, shell=True)

# while True:
#     data = client.recv(1024)
#     print(str(data))
#     if data == b"#Close":
#         break
