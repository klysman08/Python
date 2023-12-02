def fatorial(numero):
    return 1 if numero in [1, 0] else numero * fatorial(numero - 1)

x = int(input("Digite um número para calcular o FAT: "))
res = fatorial(x)

print(f'O fatorial de {x} é {res} ')
