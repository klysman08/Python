#Lsitas
#Utiliza-se [] para criar listas
#É possível alterar os elementos das listas pois são mutaveis.

#Alguns comandos 
lista1 = list() #cria uma lista vazia  
lista = [1, 2, 3, 'test']

del lista[3] #Remove o elemento na posição 3
lista.pop(1)  #Normalmente é para remover o ultimo elemento, mas é possível passar a posição

lista.append(7)  #Adiciona o elemento na ultima posição da lista
lista.insert(2, 'klysman')  #Na posição 2, adicione o seguinte argumento

if 'list' in lista:
    lista.remove('test2')  #Remove o elemento passado como argumento da lista. Remoção pelo conteúdo
                            #Remove a primeira ocorrencia do elemento.

print(lista)


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


#Lsitas dentro de listas

dados = ['klysman', 'engenharia']
pessoas = list()
pessoas.append(dados[:])

print(pessoas)
print(pessoas[0][0])

galera = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()  #Limpa a lista por completo
    
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} Não é maior de idade')
        menor += 1
print(f'Temos {maior} maiores de idede e {menor} menores de idade')
