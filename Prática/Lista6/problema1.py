
ip = list()

for i in range(0, 4):
    valor = int(input(f'Digite um valor da parte {i}: '))
    ip.append(valor)
        
        
for j in ip:
    if j > 255:
        print ('O valor digitado não é válido')
        
print(f'O IP digitado foi {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
    