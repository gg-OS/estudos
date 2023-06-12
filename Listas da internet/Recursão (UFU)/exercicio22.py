def fibonacci(n):
    if n < 1:
        return 0

    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


numero = input('Insira a quantidade de números da série de fibonacci que deseja imprimir: ')
numero = int(numero)

for i in range(1, numero):
    print(fibonacci(i))

print()
print('powered by ggOS')
