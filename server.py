# X25519 Key Exchange
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey, X25519PublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import base64

# AES Symetric Cipher
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Padding
from cryptography.hazmat.primitives import padding

import socket
from threading import Thread, Event

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysock.bind((socket.gethostname(), 8500))
mysock.listen(5)

# Setting up the cryptography
env_publickey = base64.standard_b64decode(os.environ['HIS_PUBLICKEY'].encode(encoding="utf-8", errors="strict"))
loaded_public_key = X25519PublicKey.from_public_bytes(env_publickey)
env_private_key = base64.standard_b64decode(os.environ['PRIVATEKEY'].encode(encoding="utf-8", errors="strict"))
private_key = X25519PrivateKey.from_private_bytes(env_private_key)
shared_key = private_key.exchange(loaded_public_key)
# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)
HMAC_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'hmac authentication code',
).derive(shared_key)

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
            # Récupération des données TCP entrantes
            iv_ciphertext = clientsocket.recv(512)
            # print(base64.standard_b64encode(iv_ciphertext))
            hashmac = clientsocket.recv(512)
            # print(base64.standard_b64encode(hashmac))

            # Vérification immédiate de l'intégrité du message
            h = hmac.HMAC(HMAC_key, hashes.SHA256())
            h.update(iv_ciphertext)
            h.verify(hashmac)

            # Chiffrement AES effectif
            cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv_ciphertext[:16]))
            decryptor = cipher.decryptor()
            data = decryptor.update(iv_ciphertext[16:]) + decryptor.finalize()
            # Ajout du "padding" final
            unpadder = padding.PKCS7(128).unpadder()
            message = unpadder.update(data)
            message += unpadder.finalize()
            if message.decode() == "exit":
                print("=== Le client a coupé la connection ===")
                print("Appuyez sur Entrée pour continuer")
                mainexit.set()
                break
            print("\033[1;31m",end="")
            print(message.decode(),"\033[0m")
        
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
