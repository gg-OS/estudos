p1 = input('Informe o preço do produto 1: ')
p2 = input('Informe o preço do produto 2: ')
p3 = input('Informe o preço do produto 3: ')
if p1.isnumeric() and p2.isnumeric() and p3.isnumeric():
    p1 = int(p1)
    p2 = int(p2)
    p3 = int(p3)
    if p1 < p2 and p1 < p3:
        print('O mais barato é o primeiro produto.')
    elif p2 < p1 and p2 < p3:
        print('O mais barato é o segundo produto.')
    else:
        print('O mais barato é o terceiro produto.')
else:
    print('Por favor insira apenas números: ')
