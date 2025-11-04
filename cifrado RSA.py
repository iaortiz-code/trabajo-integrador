from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generar_claves():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def cifrar_rsa(mensaje, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    cifrado = cipher.encrypt(mensaje.encode())
    return base64.b64encode(cifrado).decode()

def descifrar_rsa(cifrado, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decifrado = cipher.decrypt(base64.b64decode(cifrado))
    return decifrado.decode()
