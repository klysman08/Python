with open("texto.txt", 'r') as arquivo:
    texto = list(arquivo)
    maior = max(texto, key=len)

    maior = maior.rstrip()

    print (maior)
    print (len(maior))