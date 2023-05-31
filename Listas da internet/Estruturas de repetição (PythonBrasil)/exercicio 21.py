x = 1
contador = 0
while True:
    num = input('Insira um número: ')
    if not num.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        num = int(num)
        while x <= num:
            if num % x == 0:
                contador += 1
                x += 1
            else:
                x += 1
        if contador == 2:
            print(f'{num} é um número primo')
        else:
            print(f'{num} não é um número primo')
    cont = input('Deseja continuar? (s/n) ')
    if cont == 's':
        continue
    else:
        break
print()
print('Fim do programa.')
