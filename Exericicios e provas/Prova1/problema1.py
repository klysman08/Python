VP = float(input('Digite o valor do investimento inicial: '))
TAXA_ANO = float(input('Digite a taxa de juros anual: '))
ANOS = int(input('Digite o período do investimento em anos: '))

VF = VP * (1 + (TAXA_ANO / 100)) ** ANOS

print('Valor futuro: %.2f' % VF)