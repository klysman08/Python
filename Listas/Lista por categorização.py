#084

pessoas = list()
lista = list()

for i in range(0, 3):


    pessoas.append(str(input('Insira o nome:')))
    pessoas.append(int(input('Insira o peso:')))
    lista.append(pessoas[:])
    pessoas.clear()


pesados = list()
magros = list()

for peso in lista:
    if peso[1] >= 80:
        pesados.append(peso)
    elif peso[1] < 80:
        magros.append(peso)

print(len(lista))
print(pesados)
print(magros) 