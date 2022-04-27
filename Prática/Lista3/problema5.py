def peso_ideal(altura, sexo):
    if sexo == 'm' or sexo == 'M':
        return 72.7 * altura - 58
    elif sexo == 'f' or sexo == 'F':
        return 62.1 * altura - 44.7
    else:
        return 'Sexo inválido'