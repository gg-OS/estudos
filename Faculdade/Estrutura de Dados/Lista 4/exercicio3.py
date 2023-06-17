from math import pi


def perimetro(r):
    p = 2 * pi * r
    return p


def area(r):
    a = pi * (r ** 2)
    return a


print('Geometria ggOS')
raio = input('Insira o raio do círculo em questão: ')
raio = float(raio)
print(f'Área = {area(raio):.2f}')
print(f'Perimetro = {perimetro(raio):.2f}\n')
print('powered by ggOS')
