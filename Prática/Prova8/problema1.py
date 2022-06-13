arquivo = open ("notas.txt", 'r')
campos = []
notas = []

for linha in arquivo:
    campos.append(linha)
    nome = campos[0]
    for nota in campos[1:]:
        notas.append(nota)