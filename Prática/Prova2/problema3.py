x = int(input('Digite o comprimento do primeiro lado: '))
y = int(input('Digite o comprimento do segundo lado: '))
z = int(input('Digite o comprimento do terceiro lado: '))


if z < x+y and y < x+z and x < y+z:
    if x == y and x == z:
        print('Triângulo Equilátero')
    elif x == y or x == z or y == z:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não é um triângulo')    
