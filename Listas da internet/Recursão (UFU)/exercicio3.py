def somatorio(n):

    if n == 1:
        return 1

    return (n ** 3) + somatorio(n - 1)


numero = input('Insira um número para o somatório: ')

try:
    numero = int(numero)
    print(f'Somatório dos cubos: {somatorio(numero)}')
except ValueError:
    print('Número inválido, encerrando programa.')

print()
print('powered by ggOS')
