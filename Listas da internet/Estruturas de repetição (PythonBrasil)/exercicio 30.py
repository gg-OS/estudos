cont = 0
valor = 0
while True:
    qtd = input('Quantos itens o cliente está levando? ')
    if not qtd.isnumeric():
        print('Insira um número inteiro.')
        continue
    else:
        qtd = int(qtd)
        break
while cont < qtd:
    valor += 0.18
    cont += 1
    print(f'{cont} - R$ {valor:.2f}')
