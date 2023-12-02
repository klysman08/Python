dados = dict()
lista = []

for _ in range (0, 3):
    dados['nome'] = str(input('Digite o nome do aluno:'))
    dados['media'] = int(input('Digite a média desse aluno: '))

    dados['situação'] = 'aprovado' if dados['media'] >= 7 else 'reprovado'
    lista.append(dados.copy())

for i in lista:

    print(f'{i}')
