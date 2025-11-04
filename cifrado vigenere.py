from .base import CipherStrategy

class VigenereCipher(CipherStrategy):
    """Implementa el cifrado y descifrado de Vigenère."""

    def _extend_key(self, text, key):
        key = key.lower()
        return ''.join([key[i % len(key)] for i in range(len(text))])

    def encrypt(self, text: str, key=None) -> str:
        if not key:
            raise ValueError("Se requiere una clave para Vigenère.")
        key_extended = self._extend_key(text, key)
        result = ""
        for t, k in zip(text, key_extended):
            if t.isalpha():
                base = ord('A') if t.isupper() else ord('a')
                result += chr((ord(t.lower()) - ord('a') + ord(k) - ord('a')) % 26 + base)
            else:
                result += t
        return result

    def decrypt(self, text: str, key=None) -> str:
        if not key:
            raise ValueError("Se requiere una clave para Vigenère.")
        key_extended = self._extend_key(text, key)
        result = ""
        for t, k in zip(text, key_extended):
            if t.isalpha():
                base = ord('A') if t.isupper() else ord('a')
                result += chr((ord(t.lower()) - ord(k) + 26) % 26 + base)
            else:
                result += t
        return result
