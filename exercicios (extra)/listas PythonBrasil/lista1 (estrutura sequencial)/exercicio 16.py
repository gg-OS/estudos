import math

area = input('Informe o tamanho da área a ser pintada: ')
if not area.replace('.', '').isdigit():
    print('Por favor insira apenas números.')
area = float(area)
tinta = area / 3
balde = tinta / 18
balde = math.ceil(balde)
preco = 80 * balde
print(f'O custo dos baldes de tinta para pintura será de: {preco}R$')
