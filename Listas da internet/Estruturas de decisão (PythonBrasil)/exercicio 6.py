n1 = input('Insira um número: ')
n2 = input('Insira outro número: ')
n3 = input('Insira um último número: ')
if not n1.isnumeric() and n2.isnumeric() and n3.isnumeric():
    print('Por favor insira apenas números!')
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
