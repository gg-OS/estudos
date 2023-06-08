def somatorio(n):
    if n == 1:
        return 2

    else:
        return ((1 + pow(n, 2)) / n) + somatorio(n - 1)


numero = input('Insira o valor n para cálculo da série: ')

numero = int(numero)

resultado = somatorio(numero)

print(resultado)
