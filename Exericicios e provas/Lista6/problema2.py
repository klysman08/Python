saltos = []
for _ in range(5):
    salto = float(input('Digite um salto: '))
    saltos.append(salto)

saltos.sort()    

meio = saltos[1:-1]



media = sum(meio) / len(meio)

print(f'Média: {media:.2f}')