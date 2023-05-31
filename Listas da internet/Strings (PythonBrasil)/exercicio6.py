data = input('Insira sua data de nascimento no formato (DD/MM/AAAA): ')
dia = data[:2]
mes = data[3:5]
ano = data[6:10]
if mes == '01':
    mes = 'Janeiro'
elif mes == '02':
    mes = 'Fevereiro'
elif mes == '03':
    mes = 'Março'
elif mes == '04':
    mes = 'Abril'
elif mes == '05':
    mes = 'Maio'
elif mes == '06':
    mes = 'Junho'
elif mes == '07':
    mes = 'Julho'
elif mes == '08':
    mes = 'Agosto'
elif mes == '09':
    mes = 'Setembro'
elif mes == '10':
    mes = 'Outubro'
elif mes == '11':
    mes = 'Novembro'
elif mes == '12':
    mes = 'Dezembro'

print(f'Você nasceu em {dia} de {mes} de {ano}.')
