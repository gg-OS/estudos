n = input('Insira um numero de 1 a 7: ')
if n.isnumeric():
    n = int(n)
    if 1 <= n <= 7:
        if n == 1:
            print('Domingo')
        elif n == 2:
            print('Segunda')
        elif n == 3:
            print('Terça')
        elif n == 4:
            print('Quarta')
        elif n == 5:
            print('Quinta')
        elif n == 6:
            print('Sexta')
        else:
            print('Sábado')
    else:
        print('Apenas números de 1 a 7')
else:
    print('Apenas números de 1 a 7')
