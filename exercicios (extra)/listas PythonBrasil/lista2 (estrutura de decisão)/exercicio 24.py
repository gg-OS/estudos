import math
resultado = 0
n1 = input('Insira um numero: ')
n1 = float(n1)
n2 = input('Insira outro numero: ')
n2 = float(n2)
op = input('Insira a operação (+, -, * ou /): ')
if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    resultado = n1 / n2
else:
    print('Operação inválida.')
if (math.floor(resultado) % 2) == 0:
    print('Número par.')
else:
    print('Número impar.')
if resultado >= 0:
    print('Positivo.')
else:
    print('Negativo.')
resultado = str(resultado)
if resultado.isnumeric():
    print('Inteiro')
else:
    print('Decimal.')
