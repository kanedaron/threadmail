import socket
import base64
from threading import Thread, Event

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# mysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysock.bind((socket.gethostname(), 8500))
mysock.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = mysock.accept()
    # now do something with the clientsocket
    print("=== Un client vient de se connecter ===")      
    print("Envoyez le message 'exit' pour terminer la conversation\n")
    # in this case, we'll pretend this is a threaded server

    mainexit = Event()

    def listener():
        while True:
            data = clientsocket.recv(512)
            data = base64.standard_b64encode(data)        
            if data.decode() == "exit":
                print("=== Le client a coupé la connection ===")
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
            clientsocket.send(mail.encode())
            break
        clientsocket.send(mail.encode())

    clientsocket.close()
    if input("exit?") == "y":
        break

mysock.close()