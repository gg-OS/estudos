n = input('Insira um numero (menor que 10000): ')
n = int(n)
c = 1
if not 0 < n < 10000:
    print('Número inválido')
else:
    while c != 10000:
        if n % c == 2:
            print(c)
        c += 1
print()
print('powered by ggOS')
