cat1 = input('Insira o valor do primeiro cateto: ')
cat2 = input('Insira o valor do segundo cateto: ')
cat1 = float(cat1)
cat2 = float(cat2)
if cat1 <= 0 or cat2 <= 0:
    print('Impossível calcular valor da hipotenusa.')
else:
    hip = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5
    print(f'Hipotenusa = {hip}')
print()
print('powered by ggOS')
