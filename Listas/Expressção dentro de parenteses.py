#083

espressao = str(input("Digite uma expressão dentro de parenteses: "))

lista = list()

for s in espressao:
    if s == '(':
        lista.append('(')

    elif s == ')':
        if len(lista) > 0:
            lista.pop()

        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Tente novamente')