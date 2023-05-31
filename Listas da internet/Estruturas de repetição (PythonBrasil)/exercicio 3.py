x = 0
while True:
    nome = input('Insira seu nome: ')
    if len(nome) < 3:
        print('Nome inválido.')
        continue
    else:
        break
while True:
    idade = input('Insira sua idade: ')
    if not idade.isnumeric():
        print('Insira sua idade de forma válida.')
    else:
        idade = int(idade)
        if 0 > idade or idade > 150:
            print('Insira uma idade realística.')
            continue
        else:
            break
while True:
    salario = input('Insira seu salário: ')
    if not salario.replace('.', '').isnumeric():
        print('Insira apenas números')
        continue
    else:
        salario = float(salario)
        break
while True:
    sexo = input('Insira seu sexo (M ou F): ')
    sexo = sexo.title()
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print('Sexo inválido.')
        continue
while True:
    estado = input('Insira seu estado civil (s, c, v ou d): ')
    if estado == 's' or estado == 'c' or estado == 'v' or estado == 'd':
        break
    else:
        print('Estado civil inválido.')
print(nome.title())
print(idade)
print(f'{salario:.2f}')
print(sexo)
print(estado)
