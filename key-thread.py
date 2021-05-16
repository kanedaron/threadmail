from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives import serialization
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
# Generate a private key for use in the exchange.
private_key = X25519PrivateKey.generate()
public_key = private_key.public_key()

private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
)

privateFile = open("privatekey", "x")
publicFile = open("publickey", "x")
privateFile.write(str(base64.standard_b64encode(private_bytes), encoding="utf-8"))
publicFile.write(str(base64.standard_b64encode(public_bytes), encoding="utf-8"))
privateFile.close()
publicFile.close()

# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key and
# get a public key from that. Note that in a DH handshake both peers
# must agree on a common set of parameters.
loaded_public_key = X25519PrivateKey.from_public_bytes(peer_public_key)
shared_key = private_key.exchange(loaded_public_key)
# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)


# For the next handshake we MUST generate another private key.
# private_key_2 = X25519PrivateKey.generate()
# peer_public_key_2 = X25519PrivateKey.generate().public_key()
# shared_key_2 = private_key_2.exchange(peer_public_key_2)
# derived_key_2 = HKDF(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=None,
#     info=b'handshake data',
# ).derive(shared_key_2)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import base64

private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption(),
)
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
)

privateFile = open("privatekey", "x")
publicFile = open("publickey", "x")
privateFile.write(str(base64.standard_b64encode(private_bytes), encoding="utf-8"))
publicFile.write(str(base64.standard_b64encode(public_bytes), encoding="utf-8"))
privateFile.close()
publicFile.close()