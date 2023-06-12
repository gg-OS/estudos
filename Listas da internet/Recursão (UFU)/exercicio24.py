def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


numero = input('Insira a quantidade de números da série de tribonacci que deseja imprimir: ')
numero = int(numero)

for i in range(1, numero):
    print(tribonacci(i))

print()
print('powered by ggOS')
