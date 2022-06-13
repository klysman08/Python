from datetime import date

arquivo = open("texto.txt", 'r')
data = []
datas = []
lista_datas = []
nomes = []
hoje=[2019,10,23]
idades = []

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

ages = []

for k in lista_datas:
    ano = hoje[0] - k[0]
    idades.append(ano)

    d0 = date(k[0], k[1], k[2])
    d1 = date(hoje[0], hoje[1], hoje[2])
    delta = d1 - d0

    ages.append(delta)

agora = ages[0]
print(agora.year)

for n in range(0,4):
    print (f'Nome: {nomes[n]}')
    print (f'Idade: {idades[n]} anos')



arquivo.close()

