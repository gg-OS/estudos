def coluna(num):
    string = ''
    for cont in range(num):
        string += str(num) + ' '
    print(string)


x = ''
n = input('Insira um número inteiro: ')
while not n.isnumeric():
    print('Número inválido')
    n = input('Insira um número inteiro: ')
n = int(n)
for i in range(1, n + 1):
    coluna(i)
