a = input('Insira um numero: ')
if not a.isnumeric():
    print('NUMERO')
else:
    a = int(a)
b = input('Insira outro numero: ')
if not b.isnumeric():
    print('NUMERO')
else:
    b = int(b)
if a > b:
    print(a)
else:
    print(b)
