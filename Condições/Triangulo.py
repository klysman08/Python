a = int(input('Digite a primeira medida '))
b = int(input('Digite a segunda medida '))
c = int(input('Digite a terceira medida'))

if a < b+c and b < a+c and c < a+b:
    print('Parabens')
else:
    print('Impossível formar o triangulo')