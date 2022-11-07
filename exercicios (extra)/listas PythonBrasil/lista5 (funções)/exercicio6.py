def turno(x):
    if x > 12:
        hora_conv = x - 12
        horario = str(hora_conv) + ' ' + 'P.M.'
    elif x == 12:
        horario = '12 P.M.'
    elif x == 0:
        horario = '12 A.M.'
    else:
        horario = str(hora) + ' ' + 'A.M.'
    return horario


while True:
    hora = input('Insira um horário para conversão: ')
    if not hora.isnumeric():
        print('Insira um horário válido.\n')
        continue
    else:
        hora = int(hora)
    if hora > 24 or hora < 0:
        print('Horário inválido.\n')
        continue
    else:
        print(f'A hora convertida é: {turno(hora)}\n')
    cont = input('Deseja continuar? (Sim/Não): ')
    print()
    if cont.title() == 'Sim':
        continue
    else:
        break

print()
print('powered by ggOS®')
