def hiperfatorial(n):
    if n == 1:
        return 1

    else:
        return (n ** n) * hiperfatorial(n - 1)


numero = input('Insira um número para cálculo de hiperfatorial: ')

try:

    numero = int(numero)
    resultado = hiperfatorial(numero)
    print(f'H({numero}) = {resultado}')

except ValueError:

    print('Número inválido. Encerrando programa...')

print('powered by ggOS')