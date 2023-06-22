import math
vendedor = 0
fim = '0'
vendido = []
dados = [0] * 9
while fim == '0':
    valor = input(f'Insira o valor das vendas do vendedor #{vendedor + 1}: ')
    valor = float(valor)
    vendido.append(200 + (valor * 0.09))
    vendedor += 1
    fim = input('Insira 0 se deseja continuar: ')

for v in vendido:
    h = math.floor(v / 100)
    if h > 8:
        h = 8
    elif h < 0:
        h = 0
    dados[h] += 1

print()
print(dados)
