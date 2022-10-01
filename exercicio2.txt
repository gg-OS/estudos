cat1 = input('Insira o valor do primeiro cateto: ')
cat2 = input('Insira o valor do segundo cateto: ')
hip = input('Insira o valor da hipotenusa: ')
cat1 = float(cat1) ** 2
cat2 = float(cat2) ** 2
hip = float(hip) ** 2
if cat1 <= 0 or cat2 <= 0 or hip <= 0:
    print('Não é um triângulo')
elif hip == cat1 + cat2:
    print('Triângulo Retângulo')
else:
    print('Triângulo não retângulo')
print()
print('powered by ggOS')
