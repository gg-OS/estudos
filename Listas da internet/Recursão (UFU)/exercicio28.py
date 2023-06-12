def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print('Insira dois números para cálculo da função de Ackerman.')
n1 = input('Insira n1: ')
n2 = input('Insira n2: ')

try:

    n1 = int(n1)
    n2 = int(n2)
    if n2 < n1:
        print('O segundo número deve ser maior que o primeiro.')
    else:
        print(f'A({n1},{n2}) = {ackermann(n1, n2)}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
