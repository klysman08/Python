pedro = float(input('Digite o valor que o Pedro apostou: '))
joao = float(input('Digite o valor que o João apostou: '))
marcela = float(input('Digite o valor que a Marcela apostou: '))

premio = float(input('Digite o valor do prêmio: '))

proporcial_total = pedro + joao + marcela

recebe_pedro = premio * (pedro / proporcial_total)
recebe_joao = premio * (joao / proporcial_total)
recebe_marcela = premio * (marcela / proporcial_total)

print('Prêmio do Pedro: %.2f' % recebe_pedro)
print ('Prêmio do João: %.2f' % recebe_joao)
print ('Prêmio da Marcela: %.2f' % recebe_marcela)
