#082

lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número para lista e 0 para sair: '))

    if n == 0:
        break

    lista.append(n)

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])

for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Lista completa {lista}')
print(f'Lista par {listapar}')
print(f'Lista impar {listaimpar}')