with open("notas.txt", "r") as arquivo:
    medias = []
    for linha in arquivo:
        campos = linha.split()
        nome = campos[0]

        notas = [float(nota) for nota in campos[1:]]
        media = sum(notas) / len(notas)

        medias.append(media)


    print(max(medias))
    print(min(medias))