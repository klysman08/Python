
ip = str(input('Digite um valor da parte: '))

new_ip = ip.split('.')

results = list(map(int, new_ip))


count = 0

for j in results:
    if j < 0 or j > 255:
        print ('Inválido')
        break
    else:
        count += 1

if count == 4:
    print ('Válido')

""" print(f'O IP digitado foi {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}') """
