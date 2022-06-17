par = []
impar = []
lista = []

for i in range(0, 5):
    valor = int(input(f'Digite o {i} valor: '))
    lista.append(valor)
    
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
 
print(lista)       
print(par)
print(impar)