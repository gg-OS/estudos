n1 = input('Insira um número: ')
n2 = input('Insira outro número: ')
n3 = input('Insira um último número: ')
if not n1.isnumeric() or not n2.isnumeric() or not n3.isnumeric():
    print('Por favor insira apenas números!')
else:
    if n1 > n2 and n1 > n3:
        print(f'O maior número é: {n1}')
        if n2 > n3:
            print(f'O menor número é: {n3}')
        else:
            print(f'O menor número é: {n2}')
    elif n2 > n1 and n2 > n3:
        print(f'O maior número é: {n2}')
        if n1 > n3:
            print(f'O menor número é: {n3}')
        else:
            print(f'O menor número é: {n1}')
    else:
        print(f'O maior número é: {n3}')
        if n1 > n2:
            print(f'O menor número é: {n2}')
        else:
            print(f'O menor número é: {n1}')
