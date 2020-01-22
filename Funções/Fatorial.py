def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return  numero * fatorial(numero - 1)

x = int(input("Digite um número para calcular o FAT: "))
res = fatorial(x)

print('O fatorial de {} é {} '.format(x, res))
