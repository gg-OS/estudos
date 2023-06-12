from math import floor


def binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return binario(floor(n / 2)) + str(n % 2)


numero = input('Insira um número para converter em binário: ')

try:

    numero = int(numero)
    print(f'bin({numero}) = ({binario(numero)})')

except ValueError:

    print('Número inválido. Encerrando programa...')

print()
print('powered by ggOS')
