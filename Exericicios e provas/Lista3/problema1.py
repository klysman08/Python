# -*- coding: utf-8 -*-

def pagamento(salario):
	if salario <= 280: 
		return salario * 1.2
	elif salario <= 700:
		return salario * 1.15
	elif salario <= 1500:
		return salario * 1.1
	else:
		return salario * 1.05


