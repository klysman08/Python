vetor_a = []
vetor_b = []
n = int(input('Digite a dimensão: '))
produto = 0
for _ in range(0,n):
    valor = int(input('Dimensão: '))
    vetor_a.append(valor)

for _ in range(0,n):
    valor = int(input('Dimensão: '))
    vetor_b.append(valor)


for k in range(0, n):
    produto = (vetor_a[k]*vetor_b[k]) + produto

print(f'Produto Escalar: {produto}')