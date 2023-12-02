#61 Super PA
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão r da PA: '))
i = 1

print(f'O 1 termo da PA é: {a}')
while (i < 10):
    a = a + r
    i += 1
    print(f'O {i} termo da PA é: {a}')

n = 1

while (n != 0):

    n = int(input('Gostaria de mais termos na PA? Quantos: '))
    s  = i + n
    while (i < s):
        a = a + r
        i += 1
        print(f'O {i} termo da PA é: {a}')

print ('Programa finalizado')