

custo = float(input('Digite o custo de fábrica: '))

if custo <= 12000:
    custo_total = custo*1.05
elif custo <= 25000:
    custo_total = custo*1.25
else:
    custo_total = custo*1.35
print('Custo total %.2f' %custo_total)	
     
