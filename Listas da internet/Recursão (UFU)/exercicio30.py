def catalan(n):
    if n == 0:
        return 1
    else:
        return (2 * ((2 * n) - 1)) / (n + 1) * catalan(n - 1)


numero = input('Insira a quantidade de números da série de catalan que deseja imprimir: ')
numero = int(numero)

for i in range(1, numero):
    print(f'{catalan(i):.0f}')

print()
print('powered by ggOS')
