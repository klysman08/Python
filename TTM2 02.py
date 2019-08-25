""" Escreva um programa que pergunte ao usuário quantos númerosde Fibonacci
serão gerados.Aproveite esta oportunidade para pensar sobre como você pode
usar funções.Certifique - se de pedir ao usuário para inserir o númerode números na
sequencia para gerar.
(Dica: A sequencia Fibonacci é uma série onde o próximo número na sequencia é a
soma dos dois números anteriores da série.E assim: 1, 1, 2, 3, 5, 8, 13, ...). """

n = int(input("Digite um numero para a sua função Fibonacci: "))
n1 = 0
n2 = 1

print(f' {n1} -> {n2}', end='')

cont = 3
while cont <= n+1:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(f' -> {n3}', end='')


