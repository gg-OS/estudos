n = input('Insira um numero: ')
c = 1
n = int(n)
while c != (n + 1):
    if n % c == 0:
        print(c)
    c += 1
print()
print('powered by ggOS')
