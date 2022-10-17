numero = input('Insira um número inteiro menor que 1000: ')
if not numero.isnumeric():
    print('Insira um número inteiro menor que 1000')
else:
    print(f'Centenas: {numero[0]}')
    print(f'Dezenas: {numero[1]}')
    print(f'Unidades: {numero[2]}')