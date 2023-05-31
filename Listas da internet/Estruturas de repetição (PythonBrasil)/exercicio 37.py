# Codigo, altura e peso
# Quando digitar 0, encerrar o programa
alto = ''
baixo = ''
gordo = ''
magro = ''
maior_a = 0
menor_a = 999
maior_p = 0
menor_p = 999
while True:
    while True:
        codigo = input('Insira seu código de aluno: ')
        while not codigo.isnumeric():
            print('Por favor insira seu código corretamente.')
            print()
            codigo = input('Insira seu código de aluno: ')
        if codigo == '0':
            break
        peso = input('Insira seu peso em kg: ')
        while not peso.replace('.', '').isnumeric():
            print('Por favor insira seu peso corretamente.')
            print()
            peso = input('Insira seu peso em kg: ')
        peso = float(peso)
        altura = input('Insira sua altura em m: ')
        while not altura.replace('.', '').isnumeric():
            print('Por favor insira sua altura corretamente.')
            print()
            altura = input('Insira sua altura em m: ')
        altura = float(altura)
        break
    if altura > maior_a:
        maior_a = altura
        alto = codigo
    elif altura < menor_a:
        menor_a = altura
        baixo = codigo
    if peso > maior_p:
        maior_p = peso
        gordo = codigo
    elif peso < menor_p:
        menor_p = peso
        magro = codigo
    if codigo == '0':
        break
print(f'Magro: {magro} / {menor_p} kg')
print(f'Gordo: {gordo} / {maior_p} kg')
print(f'Alto: {alto} / {maior_a} m')
print(f'Baixo: {baixo} / {menor_a} m')

# Para casos como esse, talvez seja interessante colocar um while de inserção de dados
# no final do código, para poder aplicar o break sem problemas estruturais