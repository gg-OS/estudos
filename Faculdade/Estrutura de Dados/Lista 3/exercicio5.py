numeros = []
par = []
impar = []
n = 0
while n < 20:
    num = input('Insira um número inteiro: ')
    if num.isnumeric():
        num = int(num)
        n += 1
        numeros.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    else:
        print('Número inválido.')
        print()
        continue
print(f'Números: {numeros}')
print(f'Pares: {par}')
print(f'Impares: {impar}')
