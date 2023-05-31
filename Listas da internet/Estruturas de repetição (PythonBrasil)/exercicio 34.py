x = 1
cont = 0
while True:
    numero = input('Insira um número: ')
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Insira um número inteiro.')
        continue
while x <= numero:
    if numero % x == 0:
        cont += 1
        x += 1
    else:
        x += 1
if cont == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')
