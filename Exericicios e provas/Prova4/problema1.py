n = int(input('Digite um número: '))
divisores = sum(i for i in range(1,n+1) if n%i == 0)
divisores = divisores - n
print(f'Resultado: {divisores}') 