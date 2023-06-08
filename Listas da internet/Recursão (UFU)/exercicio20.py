def fatorial_exp(n):
    if n == 1:
        return 1

    else:
        return n ** fatorial_exp(n - 1)


numero = input('Insira um número para cálculo de fatorial exponencial: ')

try:

    numero = int(numero)
    resultado = fatorial_exp(numero)
    print(f'Fatorial exponencial = {resultado}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
