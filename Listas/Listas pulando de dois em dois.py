#Cria uma lista de 4 a 11 pulando de dois em dois
valores = list(range(4, 11, 2)) 

print(valores)

valores.sort()  #Ordena os valores de uma lista
valores.sort(reverse=True)  #Ordena pelo inverso
len(valores)  #Me infoma o tamnho da lista

print(valores)
print('***'*30)
listaA = [1, 2, 3, 4, 5]
listaB = listaA #Cria uma ligação entre as listas. Tudo que for alterado em uma será alterado na outra
listaC = listaA[:]  #Copia a lista A para uma nova lista
listaC.append(4)
print(listaA)
print(listaC)

print('***' * 30)
print('***'*30)