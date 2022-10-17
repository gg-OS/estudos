salario = input('Insira o valor do seu salário(hora): ')
horas = input('Insira a quantidade de horas trabalhadas no mês: ')
if not horas.isnumeric():
    print('A quantidade de horas deve ser um número inteiro')
else:
    salario = float(salario)
    horas = int(horas)
    total = salario * horas
    print(f'De acordo com os dados informados, seu salário será de {total:.2f} reais')
