from .base import CipherStrategy

class CaesarCipher(CipherStrategy):
    """Implementa el cifrado y descifrado de César"""

    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt(self, text: str, key=None) -> str:
        shift = int(key) if key else self.shift
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

    def decrypt(self, text: str, key=None) -> str:
        shift = int(key) if key else self.shift
        return CaesarCipher(-shift).encrypt(text)
