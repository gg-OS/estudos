salario = input('Qual seu salário por hora? ')
horas = input('Quantas horas você trabalhou neste mês? ')
if not salario.replace('.', '').isdigit():
    print('Por favor insira um valor numérico.')
else:
    salario = float(salario)
if not horas.isnumeric():
    print('Por favor insira as horas em número inteiro')
else:
    horas = int(horas)

    salario_mes = salario * horas
    inss = salario_mes * 0.08
    irpf = salario_mes * 0.11
    sindicato = salario_mes * 0.05
    salario_liquido = salario_mes - inss - irpf - sindicato
    print(f'+ Salário Bruto: {salario_mes}R$')
    print(f'- IR (11%) : {irpf:.2f}R$')
    print(f'- INSS (8%) : {inss:.2f}R$')
    print(f'- Sindicato (5%) : {sindicato:.2f}R$')
    print(f'= Salário Líquido : {salario_liquido:.2f}R$')
