def encontra_menor(array, m):
    if len(array) == 0:
        return m

    if array[0] < m:
        m = array[0]

    del array[0]

    return encontra_menor(array, m)


lista = [7, 5, 8, 3, 2, 5, 1, -2]
menor = lista[0]

resultado = encontra_menor(lista, menor)

print(resultado)

print('powered by ggOS')
