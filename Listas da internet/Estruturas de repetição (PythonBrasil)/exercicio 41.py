p = 1
taxa = 1
while True:
    divida = input('Insira o valor da dívida: ')
    if not divida.replace('.', '').isnumeric():
        print('Dados inválidos')
        continue
    else:
        divida = float(divida)
        break
while p < 12:
    juros = divida * (1 - taxa)
    parcela = (divida - juros) / p
    if p == 1:
        print(f'{divida - juros:.2f} / {-juros:.2f} / {p} / {parcela:.2f}')
        taxa = 1.1
    elif p % 3 == 0:
        print(f'{divida - juros:.2f} / {-juros:.2f} / {p} / {parcela:.2f}')
        taxa += 0.05
    p += 1
