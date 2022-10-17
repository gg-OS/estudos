salario = input('Informe seu salário: ')
if salario.replace('.', '').isnumeric():
    salario = float(salario)
    if salario <= 280:
        aumento = 1.2
        salario_novo = salario * aumento
    elif 280 < salario <= 700:
        aumento = 1.15
        salario_novo = salario * aumento
    elif 700 < salario <= 1500:
        aumento = 1.1
        salario_novo = salario * aumento
    else:
        aumento = 1.05
        salario_novo = salario * aumento
    print(f'Salário anterior: {salario:.2f}R$')
    print(f'Aumento aplicado: {(aumento - 1) * 100:.0f}%')
    print(f'Valor do aumento: {(salario_novo - salario):.2f}R$')
    print(f'Salário novo: {salario_novo:.2f}R$')
else:
    print('Por favor insira um número válido.')
