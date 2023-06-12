def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * pell(n - 1) + pell(n - 2)


numero = input('Insira um número para calcular a função de pell: ')

try:

    numero = int(numero)
    print(f'p({numero}) = {pell(numero)}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
