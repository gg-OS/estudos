def ret(linha, coluna):
    matriz = []
    for l1 in range(0, linha):
        matriz.append([])
        for c1 in range(0, coluna):
            matriz[l1].append('')
    for l2 in range(0, linha):
        for c2 in range(0, coluna):
            if l2 == 0 or l2 == linha - 1:
                if c2 == 0 or c2 == coluna - 1:
                    matriz[l2][c2] = '+'
                else:
                    matriz[l2][c2] = '-'
            else:
                if c2 == 0 or c2 == coluna - 1:
                    matriz[l2][c2] = '|'

    for lf in range(0, linha):
        for cf in range(0, coluna):
            print(f'{matriz[lf][cf]:^2}', end='')
        print()


dim = input('Insira as dimensões do retângulo (HHxLL) sendo o máximo de 20: ')
altura = dim[:2]
largura = dim[3:]
if not altura.isnumeric() and not largura.isnumeric():
    print('Dados inválidos.')
else:
    altura = int(altura)
    largura = int(largura)
    if 20 < largura < 1 or 20 < altura < 1:
        print('Tamanho inválido.')
    ret(altura, largura)

