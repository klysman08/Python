valor_do_produto = float(input('Digite o valor do produto: '))
estado = str(input('Digite o estado: '))

if estado == 'SP' or estado == 'sp':
    valor_do_produto = valor_do_produto + (valor_do_produto * 0.12)
    print('O valor final: %.2f' % valor_do_produto)
elif estado == 'MG' or estado == 'mg':
    valor_do_produto = valor_do_produto + (valor_do_produto * 0.07)
    print('O valor final: %.2f' % valor_do_produto)
elif estado == 'RJ' or estado == 'rj':
    valor_do_produto = valor_do_produto + (valor_do_produto * 0.15)
    print('O valor final: %.2f' % valor_do_produto)
elif estado == 'MS' or estado == 'ms':
    valor_do_produto = valor_do_produto + (valor_do_produto * 0.08)
    print('O valor final: %.2f' % valor_do_produto)
else:
    print('Estado inválido')