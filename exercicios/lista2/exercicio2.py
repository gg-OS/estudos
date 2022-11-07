c1 = input('Insira o valor do primeiro cateto: ')
c2 = input('Insira o valor do segundo cateto: ')
c1 = float(c1)
c2 = float(c2)
if c1 <= 0 or c2 <= 0:
    print('Os catetos devem possuir valor positivo.')
else:
    hipotenusa = ((c1 ** 2) + (c2 ** 2)) ** 0.5
    print(f'O valor da hipotenusa é de {hipotenusa}')
print()
print('powered by ggOS')
