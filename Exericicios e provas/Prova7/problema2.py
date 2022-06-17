arquivo = open("texto.txt", 'r')

n = int(input("Digite o número n: ")) 

lista = []
l = []

for linha in arquivo:
    l = linha.split()
    for palavra in l:
        lista.append(palavra)

for c in lista:
    if len(c) <= n:
        print(c)


arquivo.close()