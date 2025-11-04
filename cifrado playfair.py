import string

def generar_matriz(clave):
    clave = clave.upper().replace("J", "I")
    matriz = []
    alfabeto = string.ascii_uppercase.replace("J", "")
    usada = ""
    for c in clave + alfabeto:
        if c not in usada and c.isalpha():
            usada += c
            matriz.append(c)
    return [matriz[i:i+5] for i in range(0, 25, 5)]

def buscar_pos(matriz, letra):
    for i, fila in enumerate(matriz):
        if letra in fila:
            return i, fila.index(letra)

def cifrar_playfair(texto, clave, modo="cifrar"):
    texto = texto.upper().replace("J", "I").replace(" ", "")
    if modo == "cifrar":
        pares = []
        i = 0
        while i < len(texto):
            a = texto[i]
            b = texto[i+1] if i+1 < len(texto) else "X"
            if a == b:
                pares.append(a + "X")
                i += 1
            else:
                pares.append(a + b)
                i += 2
    else:
        pares = [texto[i:i+2] for i in range(0, len(texto), 2)]

    matriz = generar_matriz(clave)
    resultado = ""

    for par in pares:
        a, b = par
        fila1, c
