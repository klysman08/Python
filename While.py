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


#######################################################################


#EXERCICIOS


""" 
i = 0
while (i != 'M' and i != 'F'):
     i = str(input('Digite seu genero: ')).upper().strip()[0]
print("Registrado")  """

""" 
sexo = str(input('Digite seu genero: ')).stip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. tente novamente: '))
print ('Genero {} registrado com sucesso.'.format(sexo)) """



""" 58 sorteio
from random import randint
i = 0
u = int(randint(0, 10))
contador = 0
while (i != u):
    i = int(input('Escolha um numero de 0 a 10: '))
    contador += 1

print('Acertou!')
print('Você chutou {} vezes até acertar!'.format(contador)) """

""" 59 menu de opçoes
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
    elif:
        print('Opçao invalida, tente novamente!')

print('Saindo do programa') """


""" 60 Fatorial
x = int(input('Escolha um numero para o seu fatorial: '))
i = 0
n = 1
while (i < x):
    n = (x - i) * n
    i = i + 1
print ('O fatorial de {} é {}'.format(x,n)) """

""" 61 Super PA
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

print ('Programa finalizado') """


"""  # 63 Fibonnaci  nao consegui
n = int(input('Diginte um numero para sua sequência de fibonacci: '))
t1 = 0
t2 = 1
i = 3
print('- {}\n- {}'.format(t1, t2))

while (i <= n):
    t3 = t1 + t2
    print('- {}'.format(t3))
    t1 = t2
    t2 = t3
    i += 1 """

""" 64
a = 0
contador = 0
soma = 0

while (a != 999):
    a = int(input('Digite um numero: '))
    if ( a != 999):
        soma += a

    contador += 1

print('A quantidade de numeros digitados foi {} e a soma deles é {}'.format(contador - 1, soma)) """
    

 # 65 media maior e menor
contador = 0
soma = 0
n = 1

while (n != 0):
    n = int(input('Digite um numero qualquer e 0 para o resultado: '))
    if ( n != 0 ):
        soma += n
        contador += 1
        if (contador == 1):
            n = maior = menor = 1
        else:
            if (n > maior):
                maior = n
            if (n < menor):
                menor = n

media = soma / contador
print('A média de todos o valores digitados é: {}'.format(media))
print ('O menor valor digitado foi {} e o maior for {}'.format(menor, maior)) 