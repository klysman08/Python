#089
lista = []
i = j = 0
while True:
    nome = str(input('Qual o nome do aluno: '))
    nota1 = int(input('Qual a primeira nota: '))
    nota2 = int(input('Qual a segunda nota: '))
    media = (nota1 + nota2) // 2

    lista.append([nome, [nota1, nota2] , media])

    resposta = str(input('Quer continuar? [n/s]'))
    if resposta in 'Nn':
        break

print(lista)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('*' * 20)

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    aluno = int(input('Mostrar notas de qual aluno? (digite 99 para sair)'))
    print(f'Notas do aluno {lista[aluno][0]} foram {lista[aluno][1]}')

    if aluno == 99:
        break


