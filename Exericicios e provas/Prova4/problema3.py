import math

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
count = 0

while x <= y:

    quadrado_perfeito = math.sqrt(x)
    if int(quadrado_perfeito + 0.5) ** 2 == x:
        print(x)
  
    x += 1