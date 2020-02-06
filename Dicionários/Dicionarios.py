#Semelhantes as listas
#É possível modificar os indices para litarias "identificadores"
#É identificado por chaves {}

""" dados = dict()
dados = {'nome': 'Klysman', 'idade': 25}
print(dados['nome'])

dados['sexo'] = 'M' #Não é necessairio append para criar um novo index na lista dicionario
#del dados['idade']  #Comando para remover o elemento do dicionario

dados.values()  #Retorna os elementos associados aos index
dados.keys()  #Retorna os identificadores de cada index do dicionario
dados.items()  #Retorna tanto os elementos quando os identificadoes 

for k, v in dados.items(): # printa o identificador e o elemnto associado
    print(f'O {k} é {v}') """


#Exemplos

estado = dict()
lista = list()

for c in range(0, 3):
    estado['UF'] = str(input('Nome do estado: '))
    estado['sigla'] = str(input('Qual a sigla: '))
    estado['Numero'] = str(input('Qual o numero: '))
    lista.append(estado.copy())
    
print(lista)

for e in lista:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

#Função para retornar os valores do dicionario
print(estado.values())

#Função para retornar quais são as chaves do dicionario
print(estado.keys())

#Função para retornar o valeus e keys
print(estado.items())

for k, v in estado.items():
    print(f' {k} = {v}')
