soma = 0
cont = 1
while True:
    x = input('Insira a quantidade de notas: ')
    if not x.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        x = int(x)
        break
while cont <= x:
    nota = input(f'Insira a nota #{cont}: ')
    if not nota.replace('.', '').isnumeric():
        print('Insira apenas números positivos.')
        continue
    else:
        nota = float(nota)
        soma += nota
        cont += 1
print(f'Média = {soma / x:.1f}')
