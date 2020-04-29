from time import sleep
from random import randint
from operator import itemgetter

dicionario = dict()
lista = list()

""" for c in range (0, 4):
    
    dicionario['jogador'] = str(input('Qual o nome do jogador: '))
    dicionario['dado'] = randint(1,6)
    lista.append(dicionario.copy()) """

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking) 

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

""" print(lista)
for i in lista:
    for k, v in i.items():
        print(f' {k} = {v}') """




