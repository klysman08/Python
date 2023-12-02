def peso_ideal(altura, sexo):
    if sexo in ['m', 'M']:
        return 72.7 * altura - 58
    elif sexo in ['f', 'F']:
        return 62.1 * altura - 44.7
    else:
        return 'Sexo inválido'