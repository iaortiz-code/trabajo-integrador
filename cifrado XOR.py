from .base import CipherStrategy

class XorCipher(CipherStrategy):
    """Implementa el cifrado XOR usando una clave de texto."""

    def encrypt(self, text: str, key=None) -> str:
        if not key:
            raise ValueError("Se requiere una clave para XOR.")
        key_bytes = key.encode()
        text_bytes = text.encode()
        result = bytes([t ^ key_bytes[i % len(key_bytes)] for i, t in enumerate(text_bytes)])
        return result.hex()  # Devuelve texto hexadecimal

    def decrypt(self, text: str, key=None) -> str:
        if not key:
            raise ValueError("Se requiere una clave para XOR.")
        key_bytes = key.encode()
        text_bytes = bytes.fromhex(text)
        result = bytes([t ^ key_bytes[i % len(key_bytes)] for i, t in enumerate(text_bytes)])
        return result.decode()
