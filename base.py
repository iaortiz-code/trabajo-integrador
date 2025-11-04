# Clase abstracta que define la interfaz común para todas las estrategias.
# Cada algoritmo de cifrado implementará estos métodos.

from abc import ABC, abstractmethod

class CipherStrategy(ABC):
    @abstractmethod
    def encrypt(self, text: str, key=None) -> str:
        """Cifra un texto usando la clave dada (si aplica)"""
        pass

    @abstractmethod
    def decrypt(self, text: str, key=None) -> str:
        """Descifra un texto usando la clave dada (si aplica)"""
        pass
