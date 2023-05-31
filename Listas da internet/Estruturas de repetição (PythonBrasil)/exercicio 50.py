n = input('Insira um número: ')
n = int(n)
c = 0
a = 1
b = 1
h = 0
while c < n:
    h += a/b
    a += 1
    b += 2
    c += 1
print(f'H ={h:.3f}')
