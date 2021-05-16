import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('35.189.193.125', 85))



while True:
    mail = input("entrez le message :")
    if mail == "exit":
        break
    mysock.send(mail)
    data = mysock.recv(512)
    print(data.decode())
mysock.close()