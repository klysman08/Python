arquivo = open("notas.txt", "r")
medias = []
for linha in arquivo:
    campos = linha.split()
    nome = campos[0]
    
    notas = []
    for nota in campos[1:]:
        notas.append(float(nota))
        
    media = sum(notas) / len(notas)

    medias.append(media)


print(max(medias))
print(min(medias))
arquivo.close()