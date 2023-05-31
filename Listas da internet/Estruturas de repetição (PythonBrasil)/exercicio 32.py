cont = 0
resposta = ''
fat = 1
while True:
    while True:
        numero = input('Insira o número a fazer fatorial: ')
        if not numero.isnumeric():
            print('Insira um número inteiro.')
            continue
        else:
            numero = int(numero)
            break
    while cont < numero:
        fat = fat * (numero - cont)
        letra = str(numero - cont)
        resposta += ' ' + letra + ' ' + '.'
        cont += 1
    print(f'Fatorial de {numero}:')
    print(f'{numero}! ={resposta} = {fat}')
    print()
    continuar = input('Deseja continuar? (sim/não) ')
    continuar = continuar.title()
    if continuar == 'Sim':
        continue
    else:
        break
print('ggOS company')