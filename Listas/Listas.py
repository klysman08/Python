#Lsitas
#Utiliza-se [] para criar listas
#É possível alterar os elementos das listas pois são mutaveis.

#Alguns comandos 
lista1 = []
lista = [1, 2, 3, 'test']

del lista[3] #Remove o elemento na posição 3
lista.pop(1)  #Normalmente é para remover o ultimo elemento, mas é possível passar a posição

lista.append(7)  #Adiciona o elemento na ultima posição da lista
lista.insert(2, 'klysman')  #Na posição 2, adicione o seguinte argumento

if 'list' in lista:
    lista.remove('test2')  #Remove o elemento passado como argumento da lista. Remoção pelo conteúdo
                            #Remove a primeira ocorrencia do elemento.

print(lista)






