def fatorial_duplo(n):

    if n == 1:
        return 1

    elif n % 2 == 0:
        return 1 * fatorial_duplo(n - 1)

    else:
        return n * fatorial_duplo(n - 1)


numero = input('Insira um número para cálculo de fatorial duplo: ')

try:

    numero = int(numero)
    resultado = fatorial_duplo(numero)
    print(f'{numero}!! = {resultado}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
