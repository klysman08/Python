divisores = 0 
n = int(input('digite um valor: '))
for i in range(1,n+1):
    if n%i == 0:
        divisores += i
divisores = divisores - n
print(f'Resultado: {divisores}') 