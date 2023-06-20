def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def braco(lista, i, acima):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < acima:
            if lista[i] >= max(lista[l], lista[r]):
                break
            elif lista[l] > lista[r]:
                troca(lista, i, l)
                i = l
            else:
                troca(lista, i, r)
                i = r
        elif l < acima:
            if lista[l] > lista[i]:
                troca(lista, i, l)
                i = l
            else:
                break
        elif r < acima:
            if lista[r] > lista[i]:
                troca(lista, i, r)
                i = r
            else:
                break
        else:
            break


def heapsort(lista):
    for j in range(len(lista)-2//2, -1, -1):
        braco(lista, j, len(lista))

    for fim in range(len(lista)-1, 0, -1):
        troca(lista, 0, fim)
        braco(lista, 0, fim)


produtos = [1999, 3499, 399, 1699, 999]

heapsort(produtos)

print(produtos)
