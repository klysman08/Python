def quantidade_pares(inicio, fim):
    contador = 0
    while inicio <= fim:
        if inicio % 2 == 0:
            contador += 1
        inicio += 1
    return contador
            

print(quantidade_pares(2, 2))