with open("texto.txt", 'r') as arquivo:
    n = int(input("Digite o número n: ")) 

    lista = []
    l = []

    for linha in arquivo:
        l = linha.split()
        lista.extend(iter(l))
    for c in lista:
        if len(c) >= n:
            print(c)