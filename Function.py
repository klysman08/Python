import math
def dist(a, b, c, d):
        s = 0
        s = (a - c)**2 + (b - d)**2
        dis = math.sqrt(s)
        print ('A distancia entre os dois pontos é {.2}'.format(dis))

a = int(input('Digite o ponto x de A: '))
b = int(input('Digite o ponto y de A: '))
c = int(input('Digite o potno x de B: '))
d = int(input('Digite o ponto y de B: '))


dist(a, b, c, d)