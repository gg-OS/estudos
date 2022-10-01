n = input('Insira um número até 1000: ')
n = int(n)
if 0 > n or n > 1000:
    print('Número inválido')
else:
    for i in range(0, n + 1):
        if i % 2 == 1:
            print(i)
print()
print('powered by gg0S')
