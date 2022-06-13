arquivo = open("notas.txt", "r")
for linha in arquivo:
    campos = linha.split()
    nome = campos[0]
    
    notas = []
    for nota in campos[1:]:
        notas.append(float(nota))
        
    media = sum(notas) / len(notas)
    if media >= 60:
        print (f'Nome: {nome} - Média: {media:.2f}')
            

arquivo.close()
    