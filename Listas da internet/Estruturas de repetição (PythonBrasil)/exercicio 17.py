valor = 1
num = 0
n = input('Insira o número que deseja fazer fatorial: ')
if not n.isnumeric():
    print('Caractere inválido.')
else:
    n = int(n)
    num = n
    while n > 0:
        valor = valor * n
        n -= 1
print()
print(f'O fatorial de {num} é igual a {valor} ')
