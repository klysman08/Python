dados = dict()
lista = list()

for c in range (0, 3):
    dados['nome'] = str(input('Digite o nome do aluno:'))
    dados['media'] = int(input('Digite a média desse aluno: '))
    
    if dados['media'] >= 7:
        dados['situação'] = 'aprovado'
    else: dados['situação'] = 'reprovado'
    
    lista.append(dados.copy())
    
for i in lista:

    print(f'{i}')
