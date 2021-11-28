import socket
from threading import Thread

mysock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysock.bind((socket.gethostname(), 8500))

print("=== Vous envoyez vos paquets UDP ===")

def listener():
    global mysock
    while True:
        message = str(mysock.recv(512), "utf-8")

        print("\033[1;31m",end="")
        print(message,"\033[0m")

thread = Thread(target=listener)
thread.start()

while True:
    mail = input()
    mysock.sendto(bytes(mail, "utf-8"), ('35.195.76.28', 8500))