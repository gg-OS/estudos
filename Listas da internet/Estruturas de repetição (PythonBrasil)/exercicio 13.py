x = 1
valor = 1
while True:
    base = input('Insira um numero: ')
    if not base.isnumeric():
        print('Por favor insira um numero inteiro.')
        continue
    exp = input('Insira outro numero: ')
    if not exp.isnumeric():
        print('Por favor insira um numero inteiro.')
        continue
    else:
        base = int(base)
        exp = int(exp)
        while x <= exp:
            valor = valor * base
            x += 1
        break
print(f'O resultado é: {valor}')
