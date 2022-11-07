print('Bem vindo ao posto ggOS')
print()
g = 0
a = 0
d = 0
while True:
    codigo = input('Insira o código do combustível: ')
    if not codigo.isnumeric():
        print('Código inválido')
        continue
    codigo = int(codigo)
    if not 0 < codigo <= 4:
        print('Código inválido')
        continue
    if codigo == 1:
        g += 1
    elif codigo == 2:
        a += 1
    elif codigo == 3:
        d += 1
    else:
        print()
        print('MUITO OBRIGADO')
        break
print(f'Álcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')
print()
print('powered by ggOS')
