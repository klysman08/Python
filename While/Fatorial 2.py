#60 Fatorial
x = int(input('Escolha um numero para o seu fatorial: '))
i = 0
n = 1
while (i < x):
    n = (x - i) * n
    i = i + 1
print ('O fatorial de {} é {}'.format(x,n)) 