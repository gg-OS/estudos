lado1 = input('Insira o valor do primeiro lado do triângulo: ')
lado2 = input('Insira o valor do segundo lado do triângulo: ')
lado3 = input('Insira o valor do terceiro lado do triângulo: ')
if lado1.replace('.', '').isnumeric() and lado2.replace('.', '').isnumeric() and lado3.replace('.', ''):
    if (lado1 + lado2) > lado3 and (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1:
        if lado1 == lado2 == lado3:
            print('Triangulo Equilátero')
        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 != lado1:
            print('Triângulo Isósceles')
        else:
            print('Triângulo Escaleno')
    else:
        print('Não é um triângulo válido.')
else:
    print('Por favor insira valores válidos.')
