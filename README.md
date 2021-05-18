# Threadmail

A X25519/AES secured and threaded python messenger  
Made by Nicolas Bonamour

### On the server

1. Create a python virtual environment and install required modules e.g. `pip install -r requirements.txt`
2. Create your X25519 public/private key pair with `python3 key.py`
3. Send your public key to your friend through a **secure** channel
4. Set your private key and your friend's public key as environment variables named *PRIVATEKEY* and *HIS_PUBLICKEY* by copying produced key files
    e.g. : `export PRIVATEKEY=$(cat privatekey)`
5. Set an open port as environment variable *PORT* (or just open port 8500)
6. And launch `python3 server.py`

### On the client

1. Create a python virtual environment and install required modules e.g. `pip install -r requirements.txt`
2. Create your X25519 public/private key pair with `python3 key.py`
3. Send your public key to your friend through a **secure** channel
4. Set your private key and your friend's public key as environment variables named *PRIVATEKEY* and *HIS_PUBLICKEY* by copying produced key files
    e.g. : `export PRIVATEKEY=$(cat privatekey)`
5. Set your friend's IP address and PORT as environment variables *HOST_IP* and *HOST_PORT*
6. And launch the messenger with `python3 thread.py`
