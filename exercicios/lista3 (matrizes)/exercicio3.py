matriz = []
diagonal = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        num = input('Insira um número: ')
        num = int(num)
        matriz[i].append(num)
for i in range(4):
    for j in range(4):
        print(f'[{matriz[i][j]:^2}]', end='')
        if i == j:
            diagonal += matriz[i][j]
    print()
print(f'Soma da diagonal: {diagonal}')
print()
print('powered by ggOS')
