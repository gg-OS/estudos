ano = input('Insina o ano que deseja verificar: ')
if not ano.isnumeric():
    print('Por favor insira um ano de forma válida.')
else:
    ano = int(ano)
    bissexto = ano % 4
    if bissexto == 0:
        print('O ano é bissexto.')
    else:
        print('Não é ano bissexto.')
