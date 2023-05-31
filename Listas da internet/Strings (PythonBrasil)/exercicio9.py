cpf = input('Insira seu CPF: ')
if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-' and cpf[12].isnumeric() and cpf[13].isnumeric():
    print('CPF válido')
else:
    print('CPF inválido')
