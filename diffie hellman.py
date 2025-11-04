import random

def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    claveA = pow(B, a, p)
    claveB = pow(A, b, p)
    return A, B, claveA, claveB
