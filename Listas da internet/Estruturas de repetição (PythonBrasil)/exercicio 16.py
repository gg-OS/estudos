x = 1
n1 = 0
n2 = 1
n3 = 0
while True:
    n = input('Insira a quantidade de termos: ')
    if not n.isnumeric():
        print('Por favor digite um número inteiro')
        continue
    else:
        n = int(n)
        break
while x <= n:
    print(n2)
    if n3 > 500:
        break
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    x += 1
    