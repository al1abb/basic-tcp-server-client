import socket, time, sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.30.20", int(sys.argv[1])))

name = input("Enter your name: ")

while True:
    message = input("Enter your message: ")
    full_message = f"{name}: {message}"
    client.send(full_message.encode("utf-8"))
    time.sleep(0.5)
