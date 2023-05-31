x = 1
contador = 0
div = ''
while True:
    num = input('Insira um número: ')
    if not num.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        num = int(num)
        while x <= num:
            if num % x == 0:
                div = div + str(x) + ',' + ' '
                contador += 1
                x += 1
            else:
                x += 1
        if contador == 2:
            print(f'{num} é um número primo')
        else:
            div = div[:-2]
            print(f'{num} não é um número primo')
            print(f'O número {num} é divisível por ({div})')
    cont = input('Deseja continuar? (s/n) ')
    if cont == 's':
        continue
    else:
        break
print()
print('Fim do programa.')
