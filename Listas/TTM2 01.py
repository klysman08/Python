
""" Exercício 1
Peça ao usuário para digitar
uma string e imprima se esta string é um palíndromo ou não.
(Palíndromo é uma palavra que é lida da esquerda para a direita,
conforme o sentido habitual da leitura, ou da direita para esquerda). """


lista1 = []
lista2 = []

while True:
    palavra = str(input('Digite uma palavra palíndromo: '))

    palavra2 = palavra[::-1]
    print(palavra2)


    lista1.extend(iter(palavra))
    lista2.extend(iter(reversed(palavra)))
    print(lista1)
    print(lista2)

    if lista1 == lista2:
        print('É um polindromo! ')
    else:
        print('Não é um polindromo! ')

    lista1.clear()
    lista2.clear()

    opc = int(input('Deseja continuar? [0] para sair [1] para repetir: '))
    if opc == 0:
        break
    else:
        continue
