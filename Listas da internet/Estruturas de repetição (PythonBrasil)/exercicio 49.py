n = input('Insira um número: ')
n = int(n)
c = 0
a = 1
b = 1
s = 'S = '
while c < n:
    s = s + f'{a}/{b}' + ' ' + '+' + ' '
    a += 1
    b += 2
    c += 1
print(s[:-3])
