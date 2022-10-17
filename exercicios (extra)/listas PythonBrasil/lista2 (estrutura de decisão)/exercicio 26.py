"""
Álcool - até 20 litros, 3% por litro; acima de 20 litros, 5% por litro
Gasolina - até 20 litros, 4% por litro; acima de 20 litros, 6% por litro
Álcool - 1.90 / Gasolina - 2.50
"""
qtd = input('Insira a quantidade de combustível: ')
qtd = float(qtd)
tipo = input('Insira o tipo de combustível (A/G): ')
tipo = tipo.upper()
if tipo == 'A':
    if qtd < 20:
        preco = qtd * 1.9 * 0.97
        print(f'Preço: {preco:.2f}')
    else:
        preco = qtd * 1.9 * 0.95
        print(f'Preço: {preco:.2f}')
elif tipo == 'G':
    if qtd < 20:
        preco = qtd * 1.9 * 0.96
        print(f'Preço: {preco:.2f}')
    else:
        preco = qtd * 1.9 * 0.94
        print(f'Preço: {preco:.2f}')
else:
    print('Tipo inválido.')
