'''def has_duplicates(lista1):
    if test in lista1:
        return True
    else:
        return False

lista = [1,2,3,4,6,6,6,2,1]

mylist = list(dict.fromkeys(lista))

print(mylist)
print(lista)'''


def duplicadas_em_lista(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True
    