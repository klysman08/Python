tempos = {}
melhor_tempo = float('inf')
melhor_nome = ''

arquivo = open('tempos.txt')
for linha in arquivo:
	entrada = linha.split()
	nome = entrada[0]
	soma = 0
	for tempo in entrada[1:]:
		tempo = int(tempo)
		soma += tempo

		if tempo < melhor_tempo:
			melhor_tempo = tempo
			melhor_nome = nome
	media = soma / 5
	tempos[nome] = media

lista_tempos = [(tempo, nome) for nome, tempo in tempos.items()]
lista_tempos.sort()

print('Melhor volta:', melhor_nome, '-', melhor_tempo, 'segundos')
print('Classificação final:')

for posicao, (tempo, nome) in enumerate(lista_tempos, start=1):
	print('%d - %s - %.2f' % (posicao, nome, tempo))