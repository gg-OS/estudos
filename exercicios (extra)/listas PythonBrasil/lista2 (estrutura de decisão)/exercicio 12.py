valor = input('Insira o valor da sua hora trabalhada: ')
horas = input('Insira quantas horas você trabalhou no mês: ')
if valor.replace('.', '').isnumeric() and horas.isnumeric():
    valor = float(valor)
    horas = int(horas)
    salario = valor * horas
    inss = 0.1
    fgts = 0.11
    if valor < 0 or horas < 0:
        print('Impossível ter valores negativos.')
    else:
        if salario <= 900:
            ir = 0
        elif 900 < salario <= 1500:
            ir = 0.05
        elif 1500 < salario <= 2500:
            ir = 0.1
        else:
            ir = 0.2
        salario_liquido = salario * (1 - ir - inss - fgts)
        descontos = salario * (ir + inss + fgts)
        print()
        print(f'Salário Bruto: {salario:.2f}')
        print(f'(-) IR ({int(ir * 100)}%): R$ {salario * ir:.2f}')
        print(f'(-) INSS (10%): R$ {salario * inss:.2f}')
        print(f'FGTS (11%): R$ {salario * fgts:.2f}')
        print(f'Total de descontos: R$ {descontos:.2f}')
        print(f'Salário Líquido: R$ {salario_liquido:.2f}')
else:
    print('Por favor insira dados válidos.')
