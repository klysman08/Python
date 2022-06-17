a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - (4*a*c)

if delta < 0:
    print('Não existe raiz real')
elif delta == 0:
    x = -b/(2*a)
    print('Raiz única')
    print('Raiz: %.2f' % x)
else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print('Raiz 1: %.2f' % x1)
    print('Raiz 2: %.2f' % x2)