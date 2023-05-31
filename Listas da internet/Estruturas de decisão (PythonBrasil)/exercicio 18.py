data = input('Por favor insira uma data (dd/mm/aaaa): ')
dia = data[:2]
mes = data[3:5]
ano = data[6:]
if not dia.isnumeric() or not mes.isnumeric() or not ano.isnumeric():
    print('Por favor insira a data em números.')
else:
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if dia < 0 or dia > 31:
        print('Dia inválido: ')
    elif mes < 0 or mes > 12:
        print('Mês inválido')
    elif ano < 0:
        print('Ano inválido')
    else:
        print(f'Formato de data válido. A data digitada foi {dia}/{mes}/{ano}')
