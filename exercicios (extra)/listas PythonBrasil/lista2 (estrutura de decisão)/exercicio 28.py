"""
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar

"""
total = 0
carne = input('File Duplo, Picanha ou Alcatra? ')
qtd = input('Insira o peso em kg: ')
qtd = float(qtd)
if carne.title() == 'File duplo':
    if qtd > 5:
        total = 5.8 * qtd
    else:
        total = 4.9 * qtd
elif carne.title() == 'Alcatra':
    if qtd > 5:
        total = 6.8 * qtd
    else:
        total = 5.9 * qtd
elif carne.title() == 'Picanha':
    if qtd > 5:
        total = 7.8 * qtd
    else:
        total = 6.9 * qtd
else:
    print('Carne inválida.')
print()
print(f'(+) {carne.title()} ({qtd:.1f}kg)')
print('------------------')
print(f'Subtotal: R$ {total:.2f}')
cliente = input('Você é cliente Tabajara? ')
if cliente.title() == 'Sim':
    desconto = total * 0.1
    print(f'Desconto Tabajara: R$ {desconto:.2f}')
    print(f'Total: R$ {total - desconto:.2f}')
else:
    print(f'Total: R$ {total}')
print()
print('Obrigado e volte sempre! :)')