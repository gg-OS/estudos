"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.

"""
soma = 0
cont = 0
while True:
    qtd = input('Informe a quantidade de CDs na sua coleção: ')
    if not qtd.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        qtd = int(qtd)
        break
while cont < qtd:
    preco = input(f'Insira o valor do CD#{cont + 1}: ')
    if not preco.replace('.', '').isnumeric():
        print('Insira um valor válido')
        continue
    else:
        preco = float(preco)
        soma += preco
        cont += 1
media = soma / cont
print(f'Os {qtd} CDs em sua biblioteca custaram {soma:.2f}.')
print(f'Uma média de {media:.2f} por CD.')
