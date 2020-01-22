#Lsitas dentro de listas

dados = ['klysman', 'engenharia']
pessoas = list()
pessoas.append(dados[:])

print(pessoas)
print(pessoas[0][0])

galera = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()  #Limpa a lista por completo
    
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} Não é maior de idade')
        menor += 1
print(f'Temos {maior} maiores de idede e {menor} menores de idade')