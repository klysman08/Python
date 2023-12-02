import os

with open('texto.txt', 'r') as manipulardor:
    print(manipulardor.read())

    manipulardor.seek(0)

    print('--'*20)
    print('--'*20)

    print(manipulardor.readline())
    print(manipulardor.readline())

    print('--'*20)
    print('--'*20)

    print(manipulardor.readlines())

    salve = manipulardor.readlines()

with open('texto2.txt', 'w') as arquivo:
    arquivo.writelines(salve)

with open('texto.txt', 'r') as arquivo1:
    arquivo2 = open('texto2.txt', 'w')

    salve1 = arquivo1.readlines()
    print(len(salve1))


    for linha in arquivo1:
        arquivo2.writelines(linha) #Escreve as mesmas linhas de 1 para o novo arquivo 2
        print(linha) # imprime a linha
        print(len(linha)) # tamanho da linha

    print('Arquivo copiado com sucesso!')
arquivo2.close()


#Pesquisar Palavras no texto
palavra = input('Digite a palavra para busca: ')

contador = 0

for c in arquivo2:
    c += arquivo2
    if palavra in c:
        contador = contador + 1
        print(c)
print("\n Foram retornadas" , contador, "linhas")


#Apagar arquivo
apagar = int(input('Digite 1 para apagar o arquivo ou 0 para não: '))
if apagar == 0:
    print('Arquivo não apagado')
elif apagar == 1:
    os.remove("texto2.txt")
    print('Arquivo apagado com sucesso')
else:
    print('Arquivo não encontrado')