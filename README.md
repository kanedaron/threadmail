# Threadmail

A X25519/AES secured and threaded python messenger

### On the server

1. Create your X25519 public/private key pair with `python3 key.py`
2. Send your public key to your friend through a **secure** channel
3. Set your private key and your friend's public key as environment variables named as *PRIVATEKEY* and *HIS_PUBLICKEY*
    e.g. : `export PRIVATEKEY="Thisismyprivatekey"`
4. Set an open port as environment variable *PORT* (or just open port 8500)
5. And launch `python3 server.py`

### On the client

1. Create your X25519 public/private key pair with `python3 key.py`
2. Send your public key to your friend through a **secure** channel
3. Set your private key and your friend's public key as environment variables named as *PRIVATEKEY* and *HIS_PUBLICKEY*
    e.g. : `export PRIVATEKEY="Thisismyprivatekey"`
4. Set your friend's IP address and PORT as environment variables *HOST_IP* and *HOST_PORT*
5. And launch the messenger with `python3 thread.py`
