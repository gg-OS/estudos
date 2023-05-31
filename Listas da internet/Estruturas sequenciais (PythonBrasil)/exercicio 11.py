n1 = input('Insira um número inteiro: ')
if not n1.isnumeric():
    print('Número inválido')
else:
    n1 = int(n1)
n2 = input('Insira outro número inteiro: ')
if not n2.isnumeric():
    print('Número inválido')
else:
    n2 = int(n2)
r1 = input('Insira um número real: ')
r1 = float(r1)
a = (2 * n1) * (n2 / 2)
b = (3 * n1) + r1
c = r1 ** 3
print(a)
print(b)
print(c)
