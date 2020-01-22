sexo = str(input('Digite seu genero: ')).stip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. tente novamente: '))
print ('Genero {} registrado com sucesso.'.format(sexo)) 