# É uma estrutura de repeticão por condição
# É interessante para limites desconhecidos. 

""" i = 0
while (i < 10):
    print(i)
    i = i + 1 """

""" i = 1
while (i != 0):
    i = int(input("Digite um numero: "))
print("saindo do programa") """

""" i = 1
imp = par = 0

while (i != 0):
    i = int(input("Digite um valor: "))
    if ( i != 0):
        if (i % 2 == 0):
            par += 1
        else:
            imp += 1

print("Você digitou {} pares e {} impares".format(par, imp))
"""





#EXERCICIOS

""" 57
i = 0
while (i != 'M' and i != 'F'):
     i = input('Digite seu genero: ').upper()
     i.upper()
print("Registrado") """


""" 58 
from random import randint
i = 0
u = int(randint(0, 10))
contador = 0
while (i != u):
    i = int(input('Escolha um numero de 0 a 10: '))
    contador += 1

print('Acertou!')
print('Você chutou {} vezes até acertar!'.format(contador)) """

""" 59
i = 0
a = int(input("Digite o primeiro valor: "))
b = int(input('Digite o segundo valor: '))
while (i != 5):


    print('1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Escolher outros numeros\n5 - Sair do programa\n')

    i = int(input('Escolha uma das opções: '))
    
    if (i == 1):
        soma = a + b
        print(soma)
    if (i == 2):
        mult = a * b
        print(mult)
    if (i == 3):
        if (a < b):
            print(b)
        else:
            print(a)
    if (i == 4):
        a = int(input("Digite o primeiro valor: "))
        b = int(input('Digite o segundo valor: '))
        
print('Saindo do programa') """
