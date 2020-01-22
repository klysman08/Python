#59 menu de opçoes
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

print('Saindo do programa') 