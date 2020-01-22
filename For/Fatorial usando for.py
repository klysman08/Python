
#Fatorial usando for
n = int(input('Digite um numero para calcaular o FAT: '))
s = 1
for c in range(1, n+1):
    s = s*c
print("O resultado do fatarial digitado é: {}".format(s))