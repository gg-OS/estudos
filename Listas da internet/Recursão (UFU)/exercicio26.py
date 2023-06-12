def padovan(p):
    if p == 0 or p == 1 or p == 2:
        return 1
    else:
        return padovan(p - 2) + padovan(p - 3)


numero = input('Insira a quantidade de números da série de padovan que deseja imprimir: ')
numero = int(numero)

for i in range(1, numero):
    print(padovan(i))

print()
print('powered by ggOS')
