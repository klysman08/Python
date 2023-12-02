#Lsitas dentro de listas

dados = ['klysman', 'engenharia']
pessoas = [dados[:]]
print(pessoas)
print(pessoas[0][0])

galera = []
dados = []
maior = menor = 0
for _ in range(0, 3):
    dados.extend((str(input('Nome: ')), int(input('Idade: '))))
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