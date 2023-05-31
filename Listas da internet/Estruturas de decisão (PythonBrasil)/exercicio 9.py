n1 = input('Insira um número: ')
n2 = input('Insira outro número: ')
n3 = input('Insira um último número: ')
if n1.isnumeric() and n2.isnumeric() and n3.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if n1 > n2 and n1 > n3:
        print(n1)
        if n2 > n3:
            print(n2)
            print(n3)
        else:
            print(n3)
            print(n2)
    elif n2 > n1 and n2 > n3:
        print(n2)
        if n1 > n3:
            print(n1)
            print(n3)
        else:
            print(n3)
            print(n1)
    else:
        print(n3)
        if n1 > n2:
            print(n1)
            print(n2)
        else:
            print(n2)
            print(n1)
else:
    print('Por favor insira apenas números.')
