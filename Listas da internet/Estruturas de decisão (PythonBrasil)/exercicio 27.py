"""
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
Morango
"""

morango = input('Insira o peso dos morangos: ')
morango = float(morango)
macas = input('Insira o peso das maçãs: ')
macas = float(macas)
total = 0
if morango > 5:
    total = morango * 2.2
else:
    total = morango * 2.5
if macas > 5:
    total = total + (macas * 1.5)
else:
    total = total + (macas * 1.8)
if morango + macas > 8 or total > 25:
    total = 0.9 * total
print(f'Peso total: {morango + macas}kg')
print(f'Valor total: {total} R$')
