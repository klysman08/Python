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

lista_tempos = []

for nome, tempo in tempos.items():
	lista_tempos.append((tempo, nome))

lista_tempos.sort()

print('Melhor volta:', melhor_nome, '-', melhor_tempo, 'segundos')
print('Classificação final:')

posicao = 1
for tempo, nome in lista_tempos:
	print('%d - %s - %.2f' % (posicao, nome, tempo))	
	posicao += 1