def has_duplicates(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True