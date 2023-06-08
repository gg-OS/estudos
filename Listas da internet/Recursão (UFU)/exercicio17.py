def fatorial_quadruplo(n):
    if n == 1:
        return 2

    else:
        return (2 * n) * fatorial_quadruplo(n - 1) / n * fatorial_quadruplo(n - 1)


numero = input('Insira um número para cálculo de fatorial quádruplo: ')

try:

    numero = int(numero)
    resultado = fatorial_quadruplo(numero)
    print(f'Fatorial quádruplo = {resultado}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
