#085
lista = [[],[]]

for c in range(0, 7):
    n = int(input(f'Digite o {c} numero: '))

    if n % 2 == 0:
        lista[0].append(n)

    elif n % 2 == 1:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1]) 