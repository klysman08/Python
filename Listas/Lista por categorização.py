#084

pessoas = []
lista = []

for _ in range(0, 3):
    pessoas.extend((str(input('Insira o nome:')), int(input('Insira o peso:'))))
    lista.append(pessoas[:])
    pessoas.clear()


pesados = []
magros = []

for peso in lista:
    if peso[1] >= 80:
        pesados.append(peso)
    else:
        magros.append(peso)

print(len(lista))
print(pesados)
print(magros) 