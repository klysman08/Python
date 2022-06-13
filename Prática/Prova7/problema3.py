from datetime import date, datetime

arquivo = open("/home/klysman/GitHub/Python/texto.txt", 'r')
data = []
datas = []
lista_datas = []
nomes = []

for l in arquivo:
    nome, data = l.split()
    nomes.append(nome)
    datas.append(data)

for i in datas:
    dia, mes, ano = i.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    data = [ano,mes,dia]
    lista_datas.append(data)

def calcula_idade(data_nascimento): 
    today = datetime(2021,12,31)
    age = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day)) 
    return age 

for n in range(0,len(nomes)):
    idade = lista_datas[n]
    print(f'Nome: {nomes[n]}')
    print(f'Idade: {calcula_idade(date(idade[0], idade[1], idade[2]))} anos')

arquivo.close()

