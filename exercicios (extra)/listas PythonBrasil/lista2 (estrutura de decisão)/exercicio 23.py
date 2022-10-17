import math
numero = input('Insira um número: ')
numero = float(numero)
teste = int(math.ceil(numero))
if teste == math.floor(numero) + 1:
    print('Decimal')
else:
    print('Não é decimal')
