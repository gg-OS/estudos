matriz = []
soma = 0
for i in range(3):
    matriz.append([])
    for j in range(3):
        num = input('Insira um número: ')
        num = int(num)
        matriz[i].append(num)
        soma += num
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^1}]', end='')
    print()
print()
print(f'Soma = {soma}')
print()
print('powered by ggOS')
