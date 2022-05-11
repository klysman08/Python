import math

<<<<<<< HEAD
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
count = 0

while x <= y:

    quadrado_perfeito = math.sqrt(x)
    if int(quadrado_perfeito + 0.5) ** 2 == x:
        print(x)
  
    x += 1
=======
num1 = int(input('Digite o valor de x: '))
num2 = int(input('Digite o valor de y: '))
count = 0

while count <= num2:
    n = num1+count
    
    sqrt = math.isqrt(n)
    
    if sqrt * sqrt == n:
        print(n)
    
    count = count + 1
>>>>>>> d710a08 (up)
