from math import floor


def inversor(n):
    if n < 10:
        return str(n)

    else:
        return str(n % 10) + inversor(floor(n / 10))


numero = input('Insira um número inteiro: ')

try:
    numero = int(numero)
    resultado = inversor(numero)
    print(f'Número invertido = {resultado}')
except ValueError:
    print('Você inseriu um número inválido. Encerrando o programa...')

print('powered by ggOS')
