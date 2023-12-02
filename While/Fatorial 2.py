#60 Fatorial
x = int(input('Escolha um numero para o seu fatorial: '))
n = 1
for i in range(x):
    n = (x - i) * n
print(f'O fatorial de {x} é {n}') 