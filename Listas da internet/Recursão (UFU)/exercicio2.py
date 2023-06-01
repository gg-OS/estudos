def fatorial(n):

    if n == 1:
        return 1

    return n * fatorial(n - 1)


numero = input('Insira um número para cálculo do fatorial: ')

try:
    numero = int(numero)
    print(f'{numero}! = {fatorial(numero)}')
except ValueError:
    print('Número inválido, encerrando programa.')

print()
print('powered by ggOS')
