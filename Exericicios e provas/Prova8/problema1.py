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

## ---------------------------------------------------------------

cd = input('Digite o RNA: ')
rna = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu' ,'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr', 'CAA': 'Gln'}
ami = ''
for i in range(0, len(cd), 3):
    ami = ami + rna[cd[i:i+3]] + '-'
print('Cadeia de Aminoácidos:', ami[0:-1])