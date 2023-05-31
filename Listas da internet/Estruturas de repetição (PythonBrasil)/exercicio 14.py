x = 1
impar = 0
par = 0
while x <= 10:
    numero = input('Insira um número: ')
    if not numero.isnumeric():
        print('Número inválido.')
        continue
    else:
        numero = int(numero)
        if numero % 2 == 1:
            impar += 1
            x += 1
        else:
            par += 1
            x += 1
print(f'Detectamos {impar} ímpares e {par} pares.')
