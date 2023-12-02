with open("texto.txt", 'r') as arquivo:
    texto = []

    for linha in arquivo:
        texto = linha.split()

    maior = max(texto, key=len)

    maior = maior.rstrip()

    print (maior)
    print (len(maior))