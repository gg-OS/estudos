telefone = input('Insira seu número de telefone: ')
if '-' in telefone:
    telefone = telefone.replace('-', '')
if not len(telefone) == 7 and len(telefone) == 8 and telefone.isnumeric():
    print('Aparentemente está tudo certo com seu número')
elif not len(telefone) == 7 and len(telefone) != 8:
    print('Não podemos te ajudar, insira apenas informações válidas')
elif len(telefone) == 7 and telefone.isnumeric():
    temp = telefone[3:7]
    telefone = '3' + telefone[:3]
    telefone = telefone + '-' + temp
    print(f'Telefone corrigido: {telefone}')
