#61 Super PA
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão r da PA: '))
i = 1

print ('O 1 termo da PA é: {}'.format(a))
while (i < 10):
    a = a + r
    i += 1
    print('O {} termo da PA é: {}'.format(i, a))

n = 1

while (n != 0):

    n = int(input('Gostaria de mais termos na PA? Quantos: '))
    s  = i + n
    while (i < s):
        a = a + r
        i += 1
        print('O {} termo da PA é: {}'.format(i, a))

print ('Programa finalizado')