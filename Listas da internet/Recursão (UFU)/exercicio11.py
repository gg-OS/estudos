def exibir(array, tela):

    if len(array) == 0:
        return tela

    tela += str(array[0]) + ' '
    del array[0]
    return exibir(array, tela)


n = input('Insira a quantidade de elementos: ')
lista = []
t = ''

try:
    n = int(n)
    for i in range(0, n):
        lista.append(i)
    print(exibir(lista, t))
except ValueError:
    print('\nNúmero inválido. Encerrando o programa...\n')

print('powered by ggOS')
