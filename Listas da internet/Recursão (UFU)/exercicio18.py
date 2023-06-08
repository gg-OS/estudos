def super_fatorial(n):
    if n == 1:
        return 1

    else:
        return fatorial(n) * super_fatorial(n - 1)


def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = input('Insira um número para cálculo de superfatorial: ')

try:

    numero = int(numero)
    resultado = super_fatorial(numero)
    print(f'sf({numero}) = {resultado}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
