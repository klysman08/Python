arquivo = open("texto.txt", 'r')

texto = []

for linha in arquivo:
    texto = linha.split()
    
maior = max(texto, key=len)

maior = maior.rstrip()

print (maior)
print (len(maior))

arquivo.close()