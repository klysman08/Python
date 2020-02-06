from time import sleep
from random import randint

dicionario = dict()

for c in range (0, 4):
    
    dicionario['jogador'] = str(input('Qual o nome do jogador'))
    dicionario['dado'] = randint(1,6)


for k, v in dicionario.items():
    print(f' {k} = {v}')




