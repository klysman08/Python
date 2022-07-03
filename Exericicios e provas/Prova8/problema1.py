dicionario_RNA = {'UUU':'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina','UCU':'Ser', 'UAU': 'Tyr', 'CAA':'Gln'}
lista = []

rna = str(input('Digite o RNA: '))
n = len(rna) // (len(rna) // 3 )
for index in range(0, len(rna), n):
    lista.append(rna[index: index + n])

transcricao = []

for k in lista:
    if k in dicionario_RNA:
        transcricao.append(dicionario_RNA[k])        
        
print(lista)
print(transcricao)



""" print('-'.join(str(value) for value in transcricao))
print('-'.join(str(x) for x in transcricao)) """


""" print(f'CadeiadeAminoácidos: {transcricao[0]}-{transcricao[1]}-{transcricao[2]}', end='') """

