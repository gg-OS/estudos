import math
a = input('Insira o valor a: ')
b = input('Insira o valor b: ')
c = input('Insira o valor c: ')
if a != '0':
    a = float(a)
    b = float(b)
    c = float(c)
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        x = (-b + (math.pow(delta, 1/2))) / 2 * a
        print(f'A equação só possui uma raiz real, que é: {x}')
    else:
        x1 = (-b + (math.pow(delta, 1/2))) / 2 * a
        x2 = (-b - (math.pow(delta, 1/2))) / 2 * a
        print(f'({x1}, {x2})')
elif a == '0':
    print('a = 0, não é uma equação de segundo grau.')
else:
    print('Insira apenas números.')
