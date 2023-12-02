lista = [0,1,5,78,9,4,24,6,34]

def margesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        margesort(lista, inicio, meio)
        margesort(lista, meio, fim)
        marge(lista, inicio, meio, fim)


def marge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    rigth = lista[meio:fim]

    top_left, top_rigth = 0, 0

    for k in range(inicio, fim):
        if (
            top_left >= len(left)
            or top_rigth < len(rigth)
            and left[top_left] >= rigth[top_rigth]
        ):
            lista[k] = rigth[top_rigth]
            top_rigth += 1
        else:
            lista[k] = left[top_left]
            top_left += 1


margesort(lista)
