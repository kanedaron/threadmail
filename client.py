import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('35.189.193.125', 8500))

print("=== Connecté au serveur ===")
print("Envoyez le message 'exit' pour terminer le programme\n")

while True:
    mail = input("entrez le message :")
    if mail == "exit":
        mysock.send(mail.encode())
        break
    mysock.send(mail.encode())

    #deuxieme tour

    print ("En attente du message du serveur...")
    data = mysock.recv(512)
    if data.decode() == "exit":
        print("=== Le serveur s'est déconnecté ===")
        break
    print ("\033[A                                                       \033[1;31m\033[A")
    print(data.decode(),end='\033[0m\n')
mysock.close()
