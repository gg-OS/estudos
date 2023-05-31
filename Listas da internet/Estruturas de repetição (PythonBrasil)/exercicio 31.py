cont = 1
total = 0
lista = ''
while True:
    while True:
        preco = input(f'Insira o preço do produto #{cont}: R$ ')
        if not preco.replace('.', '').isnumeric():
            print('Insira um valor válido.')
            continue
        elif preco == '0':
            break
        else:
            preco = float(preco)
            total += preco
            item = f'Produto #{cont}: R$ {preco:.2f}'
            lista += item + '\n'
            cont += 1
    print('Lojas Tabajara')
    print(lista)
    print(f'Total: R$ {total:.2f}')
    while True:
        dinheiro = input('Insira o valor pago pelo cliente: R$ ')
        if not dinheiro.replace('.', '').isnumeric():
            print('Por favor insira um valor válido.')
            continue
        else:
            dinheiro = float(dinheiro)
            if dinheiro < total:
                print('Quantia insuficiente.')
                continue
            else:
                break
    print(f'Dinheiro: R$ {dinheiro:.2f}')
    print(f'Troco: R$ {dinheiro - total:.2f}')
    print()
    continuar = input('Deseja continuar? ')
    continuar = continuar.title()
    if continuar == 'Sim':
        continue
    else:
        break
