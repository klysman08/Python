'''Escreva um programa que lê dois números inteiros,  caso o resultado tenha algum algarismo zero, então os retire antes de imprimir na
tela.'''



'''Write a program that reads two integers, if the result has any zero digits, then remove them before printing to the screen.'''
def soma_inteiros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    soma = num1 + num2
    
    soma = str(soma)
    if '0' in soma:
        new = soma.replace('0', '')
        print(new)
    else:
        print(soma)

            
soma_inteiros()