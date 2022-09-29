a = input('Insira o lado A: ')
b = input('Insira o lado B: ')
c = input('Insira o lado C: ')
if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
    print('Um dos lados inseridos é inválido.')
else:
    a = int(a)
    b = int(b)
    c = int(c)
    if a > (b + c) or b > (a + c) or c > (a + b):
        print('Triângulo inválido')
    else:
        perimetro = a + b + c
        print(f'Perimetro do triângulo: {perimetro}')
print()
print('powered by ggOS®')
