x = 1
cont = 0
y = 1
lista = ''
while True:
    numero = input('Insira um número: ')
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Insira um número inteiro.')
        continue
while x <= numero:
    cont = 0
    y = 1
    while y <= x:
        if x % y == 0:
            cont += 1
            y += 1
        else:
            y += 1
    if cont <= 2 and x != 1:
        num = str(x)
        lista += num + ',' + ' '
    x += 1
print(f'({lista[:-2]})')
