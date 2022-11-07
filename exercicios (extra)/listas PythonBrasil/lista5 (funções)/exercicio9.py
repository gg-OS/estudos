def reversor(x):
    inverso = ''
    x = str(x)
    for i in range(0, len(x)):
        inverso += x[-1 - i]
    inverso = int(inverso)
    return inverso


num = input('Insira um número: ')
if not num.isnumeric():
    print('Número inválido')
else:
    num = int(num)
    print(f'O inverso desse número é: {reversor(num)}')

print()
print('powered by ggOS®')
