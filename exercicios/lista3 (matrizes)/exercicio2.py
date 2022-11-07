matriz = []
soma = []
for i in range(3):
    matriz.append([])
    for j in range(3):
        num = input('Insira um número: ')
        num = int(num)
        matriz[i].append(num)
for i in range(3):
    soma.append(sum(matriz[i]))
    for j in range(3):
        print(f'[{matriz[i][j]:^1}]', end='')
    print()
print()
print(soma)
print()
print('powered by ggOS')
