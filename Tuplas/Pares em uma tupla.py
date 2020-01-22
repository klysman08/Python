#075

t1 = (int(input('Digite o 1 numero: ')),)
t2 = (int(input('Digite o 2 numero: ')),)
t3 = (int(input('Digite o 3 numero: ')),)
t4 = (int(input('Digite o 4 numero: ')),)
tupla = t1 + t2 + t3 + t4
print(tupla)

print(tupla.count(9))

if 3 in tupla:
    print(tupla.count(3))
    print(tupla.index(3))
else:
    print('Nenhum numero 3 digitados')

count = 0
lista = []

print('Numeros pares digitados: ')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i])
print(count)