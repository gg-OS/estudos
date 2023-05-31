y = 0
while True:
    x = input('Insira um número inteiro: ')
    if not x.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    x = int(x)
    y = input('Insira outro número inteiro: ')
    if not y.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    y = int(y)
    break
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
while menor < maior:
    print(menor)
    menor += 1
print('Fim.')
