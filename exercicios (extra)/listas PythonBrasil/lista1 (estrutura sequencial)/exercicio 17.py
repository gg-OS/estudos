import math

area = input('Informe o tamanho da área a ser pintada: ')
if not area.replace('.', '').isdigit():
    print('Por favor insira apenas números.')
area = float(area)
tinta = area / 6
balde = tinta / 18
galoes = tinta / 3.6
print(f'Caso você queira comprar apenas baldes de 18 litros, precisará de {math.ceil(balde)} baldes')
print(f'Caso você queira apenas galões de 3.6 litros, serão necessários {math.ceil(galoes)}')
print()
tinta = tinta * 1.1
balde = tinta / 18
galoes = (tinta % 18) / 3.6
preco_b = 80 * math.floor(balde)
preco_g = 25 * math.ceil(galoes)
print(f'Área a ser pintada: {area:.2f}')
print(f'Litros de tinta necessários: {tinta:.2f} (+ 10%)')
print(f'Quantidade de baldes : {math.floor(balde)}')
print(f'Quantidade de galões: {math.ceil(galoes)}')
print(f'Preço final: {preco_b + preco_g:.2f}R$')
