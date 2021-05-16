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
        if mainexit.is_set():
            break
        data = mysock.recv(512)
        if data.decode() == "exit":
            print("=== Le serveur s'est déconnecté ===")
            mysock.close()
            _thread.interrupt_main()
            break
        print("\033[1;31m",data.decode(),"\033[0m\n")

thread = Thread(target=listener)
thread.start()

while True:
    mail = input()
    if mail == "exit":
        mainexit.set()
        mysock.send(mail.encode())
    if not thread.is_alive():
        break
    mysock.send(mail.encode())


mysock.close()
