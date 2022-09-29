idade = input('Insira sua idade: ')
valor = 100

idade = int(idade)
if idade < 0:
    valor = 'Idade inválida'
elif idade <= 10:
    valor += 60
elif 10 < idade <= 30:
    valor += 90
elif 30 < idade <= 45:
    valor += 130
elif 45 < idade <= 59:
    valor += 250
else:
    valor += 400
if valor == 'Idade inválida':
    print(valor)
else:
    print(f'O valor do plano será: R$ {valor}')
print()
print('powered by ggOS®')
