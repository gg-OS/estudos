def fibonacci(n):
    if n == 0:
        return 'b'

    if n == 1:
        return 'a'

    return fibonacci(n - 1) + fibonacci(n - 2)


numero = input('Insira a quantidade de números da série de fibonacci que deseja imprimir: ')
numero = int(numero)

for i in range(0, numero):
    print(fibonacci(i))

print()
print('powered by ggOS')
