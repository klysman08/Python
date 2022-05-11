<<<<<<< HEAD
divisores = 0 
n = int(input('Digite um número: '))
for i in range(1,n+1):
    if n%i == 0:
        divisores += i
divisores = divisores - n
print(f'Resultado: {divisores}') 
=======

        
def divisores(num):
    for i in range(1, num // 2 + 1):
        if num % i == 0: 
            return i
    return num
    
    
print (divisores(9))
>>>>>>> d710a08 (up)
