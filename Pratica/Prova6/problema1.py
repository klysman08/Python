lista1 = []
lista2 = []

for i in range(0,5):
    valor = int(input('Digite um numero: '))
    lista1.append(valor)

for j in range(0,5):
    valor = int(input('Digite um numero: '))
    lista2.append(valor)

    
'''print(f'{lista1} and {lista2}')'''

intersecao =[]

for k in lista1:
    if k in lista2:
        intersecao.append(k)

print(f'Interseção: {intersecao}')