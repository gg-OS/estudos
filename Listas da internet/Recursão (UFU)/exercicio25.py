def tetranacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)


numero = input('Insira a quantidade de números da série de tetranacci que deseja imprimir: ')
numero = int(numero)

for i in range(1, numero):
    print(tetranacci(i))

print()
print('powered by ggOS')
