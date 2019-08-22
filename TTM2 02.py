""" Escreva um programa que pergunte ao usuário quantos númerosde Fibonacci
serão gerados.Aproveite esta oportunidade para pensar sobre como você pode
usar funções.Certifique - se de pedir ao usuário para inserir o númerode números na
sequencia para gerar.
(Dica: A sequencia Fibonacci é uma série onde o próximo número na sequencia é a
soma dos dois números anteriores da série.E assim: 1, 1, 2, 3, 5, 8, 13, ...). """


def fibonacci(n):
    ## Seu código
    if n <= 1:
        return (n)
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


nfib = int(input("Digite o número de termos: "))

print("Sequência de Fibonacci:")

for i in range(1, nfib+1):
    print(fibonacci(i))
