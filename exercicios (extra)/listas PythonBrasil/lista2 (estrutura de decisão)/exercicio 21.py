import math
saque = input('Informe o valor a ser sacado: ')
# 1,  5, 10, 50 e 100
# valor minimo de 10 e máximo de 600
saque = int(saque)
if saque < 10 or saque > 600:
    print('Valores indisponíveis nesse terminal')
else:
    cem = math.floor(saque / 100)
    saque = saque % 100
    cinq = math.floor(saque / 50)
    saque = saque % 50
    dez = math.floor(saque / 10)
    saque = saque % 10
    cinco = math.floor(saque / 5)
    saque = saque % 5
    um = saque
    print(f'R$ 100: {cem} ')
    print(f'R$ 50: {cinq} ')
    print(f'R$ 10: {dez} ')
    print(f'R$ 5: {cinco} ')
    print(f'R$ 1: {um} ')