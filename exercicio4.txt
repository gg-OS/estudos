cliente = 0
total = 0
negativo = 0
while cliente != 10001:
    conta = input('Insira o número da conta do cliente: ')
    if conta == '-999':
        break
    else:
        saldo = input('Insira o saldo do cliente: ')
        saldo = float(saldo)
        total += saldo
        if saldo < 0:
            negativo += 1
        cliente += 1
print()
print('Agência ggOS')
print(f'Saldo total da agência: {total:.2f}')
print(f'Número total de clientes: {cliente}')
print(f'Total de clientes negativos: {negativo}')
print()
print('powered by ggOS')
