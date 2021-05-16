import socket
import _thread
from threading import Thread, Event
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("35.240.31.174", 8500))

print("=== Connecté au serveur ===")
print("Envoyez le message 'exit' pour terminer le programme\n")

mainexit = Event()

def listener():
    global mysock
    while True:
        data = mysock.recv(512)
        if data.decode() == "exit":
            print("=== Le serveur s'est déconnecté ===")
            mainexit.set()
            break
        print("\033[1;31m",end="")
        print(data.decode(),"\033[0m\n",end="")

thread = Thread(target=listener)
thread.start()

while True:
    mail = input()
    if mainexit.is_set():
        break
    if mail == "exit":
        mysock.send(mail.encode())
        break
    mysock.send(mail.encode())


mysock.close()
