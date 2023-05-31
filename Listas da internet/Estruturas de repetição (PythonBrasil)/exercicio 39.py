x = 0
maior = 0
menor = 0
alto = ''
baixo = ''
while x < 2:
    nome = input('Insira o nome do aluno: ')
    altura = input('Insira a altura: ')
    if altura.replace('.', '').isnumeric():
        altura = float(altura)
    else:
        print('Insira uma altura válida.')
        continue
    if x == 0:
        menor = altura
        baixo = nome
    if altura > maior:
        maior = altura
        alto = nome
    elif altura < menor:
        menor = altura
        baixo = nome
    x += 1
print(f'Maior aluno: {alto} - {maior}m')
print(f'Menor aluno: {baixo} - {menor}m')
