jovem = 0
adulto = 0
idoso = 0

while True:
    idade = input('Insira a idade do participante: ')
    if not idade.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        idade = int(idade)
        if idade < 26:
            jovem += 1
        elif 26 <= idade < 60:
            adulto += 1
        else:
            idoso += 1
    continuar = input('Deseja continuar? ')
    if continuar == 'não' or continuar == 'Não':
        break
print(f'Jovens: {jovem}')
print(f'Adultos: {adulto}')
print(f'Idosos: {idoso}')
