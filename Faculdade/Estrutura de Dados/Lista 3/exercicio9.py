a = []
c = 0
soma = 0
while c < 10:
    n = input('Insira um número inteiro: ')
    if not n.isnumeric():
        print('Caractere inválido.')
        continue
    n = int(n)
    a.append(n)
    soma += (n ** 2)
    c += 1
print(a)
print(soma)