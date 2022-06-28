aluno2media = {}

while True:
    nome = input('Digite o nome do aluno: ')
    nome = nome.strip()
    if not nome:
        break
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    
    aluno2media[nome] = aluno2media.get(nome, 0) + (nota1 + nota2) / 2
    
notas = []

for aluno, media in aluno2media.items():
    notas.append((media, aluno))
notas.sort(reverse=True)

for media, aluno in notas:
    print(f'{aluno} - {media:.02f}')