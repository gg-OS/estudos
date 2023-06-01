def somatorio(n):

    if n == 0:
        return 0

    return n + somatorio(n - 1)


numero = input('Insira um número para o somatório: ')

try:
    numero = int(numero)
    print(f'Somatório: {somatorio(numero)}')
except ValueError:
    print('Número inválido, encerrando programa.')

print()
print('powered by ggOS')
