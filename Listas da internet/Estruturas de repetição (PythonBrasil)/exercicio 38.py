ano = 1996
var = 1.015
while True:
    salario = input('Digite o salário inicial: ')
    while not salario.replace('.', '').isnumeric():
        print('Salário inválido')
        salario = input('Digite o salário inicial: ')
    salario = float(salario)
    break
print(f'{ano - 1}: R${salario:.2f}')
while ano < 2022:
    if ano > 1996:
        var = 1 + ((var - 1) * 2)
    salario = salario * var
    print(f'{ano}: R${salario:.2f}')
    ano += 1
