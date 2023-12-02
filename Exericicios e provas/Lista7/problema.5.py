with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        campos = linha.split()
        nome = campos[0]

        notas = [float(nota) for nota in campos[1:]]
        media = sum(notas) / len(notas)
        if media >= 60:
            print (f'Nome: {nome} - Média: {media:.2f}')
