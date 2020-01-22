#Tuplas 
#As tuplas são imutaveis - não sendo possível alterar as variaveis nesta lista.
#Aceita tipos diferentes na tuplca, str, int, float...

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Batata', 'Tapioca')
lanche2 = ('Pudim', 'Castanhas')
lanche3 = lanche + lanche2

#metodo 1
for comida in lanche:
    print(f'Eu vou comer {comida}!')

print('-' * 50)
#metodo 2
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-'*50)
#metodo 3
for pos, comida in enumerate(lanche3):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-' * 50)

print(sorted(lanche))  # Exibe em forma de lista ordenada
print(len(lanche3))  # Exibe o tamanho da tupla
print(lanche3.count('Pudim')) #  Exibe a quantidade de vezes que o elemento aparece na tupla
print(lanche3.index('Pudim'))  # Mostra em que posição está o elemento
