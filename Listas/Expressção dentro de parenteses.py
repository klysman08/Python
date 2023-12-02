#083

espressao = str(input("Digite uma expressão dentro de parenteses: "))

lista = []

for s in espressao:
    if s == '(':
        lista.append('(')

    elif s == ')':
        if lista:
            lista.pop()

        else:
            lista.append(')')
            break

if not lista:
    print('Sua expressão está correta')
else:
    print('Tente novamente')