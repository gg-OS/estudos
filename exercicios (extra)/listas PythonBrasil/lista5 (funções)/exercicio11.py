def date(d):
    dia = d[0:2]
    mes = d[3:5]
    ano = d[6:10]
    mes = int(mes)
    if int(dia) > 31 or int(dia) < 0:
        d = 'NULL'
    elif mes > 12 or mes < 0:
        d = 'NULL'
    else:
        if mes == 1:
            mes = 'janeiro'
        elif mes == 2:
            mes = 'fevereiro'
        elif mes == 3:
            mes = 'marco'
        elif mes == 4:
            mes = 'abril'
        elif mes == 5:
            mes = 'maio'
        elif mes == 6:
            mes = 'junho'
        elif mes == 7:
            mes = 'julho'
        elif mes == 8:
            mes = 'agosto'
        elif mes == 9:
            mes = 'setembro'
        elif mes == 10:
            mes = 'outubro'
        elif mes == 11:
            mes = 'novembro'
        elif mes == 12:
            mes = 'dezembro'
        d = str(dia) + ' ' + 'de' + ' ' + mes + ' de ' + ano
    return d


data = input('Insira uma data no formato DD/MM/AAAA: ')
if date(data) == 'NULL':
    print('NULL')
else:
    print(f'{date(data)}')
