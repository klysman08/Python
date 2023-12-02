'''Faça um programa que solicite o nome do usuário e imprima-o na vertical.'''
def nome_vertical():
    nome = input('Digite seu nome: ')
    nome = list(nome)
    for item in nome:
        print(item)
        
nome_vertical()