n = input('Insira um número inteiro: ')
tam = len(n)
c = 0
s = ''
while c < tam:
    s += n[tam - 1 - c]
    c += 1
print(s)
