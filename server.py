import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind((socket.gethostname(), 8500))
mysock.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = mysock.accept()
    # now do something with the clientsocket
    print("=== Un client vient de se connecter ===")
    print("Envoyez le message 'exit' pour terminer la conversation\n")
    # in this case, we'll pretend this is a threaded server
    
    while True:
        print("En attente du message du client...")
        data = clientsocket.recv(512)
        if data.decode() == "exit":
            print("=== Le client a coupé la connection ===")
            break
        print ("\033[A                                                       \033[1;31m\033[A")
        print(data.decode(),end='\033[0m\n')
        
        #deuxieme tour

        mail = input("entrez le message :")
        if mail == "exit":
            clientsocket.send(mail.encode())
            break
        clientsocket.send(mail.encode())       
  
    clientsocket.close()
    if input("exit?") == "y":
        break

mysock.close()
