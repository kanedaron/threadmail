from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives import serialization
import base64

private_key = X25519PrivateKey.generate()
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

print("PRIVATE KEY : ")
print(str(base64.standard_b64encode(private_bytes), encoding="utf-8"))
print("PUBLICKEY : ")
print(str(base64.standard_b64encode(public_bytes), encoding="utf-8"))