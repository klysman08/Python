n = int(input("Digite um número: "))
count = 0
soma = 0
while True:
    
    count += 1
    
    if count %2==0:
        soma = soma + count
    if count == n:
        break
print(soma)