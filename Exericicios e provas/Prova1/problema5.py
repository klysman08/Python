valor = float(input('Digite o valor da compra: '))

desconto = valor * 0.9
parcela = valor / 6
comissao_v = valor * 0.9 * 0.05
comissao_p = valor * 0.05

print('Valor com desconto: %.2f ' % desconto)
print('Valor da parcela: %.2f ' % parcela)
print('Comissão do vendedor (à vista): %.2f ' % comissao_v)
print('Comissão do vendedor (parcelado): %.2f ' % comissao_p )
