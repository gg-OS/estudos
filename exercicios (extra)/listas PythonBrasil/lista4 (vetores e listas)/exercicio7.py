c = 0
soma = 0
mult = 1
numeros = []
while c < 5:
    num = input('Insira um número: ')
    if num.isnumeric():
        num = int(num)
    else:
        continue
    numeros.append(num)
    c += 1
for numero in numeros:
    soma += numero
    mult *= numero
print()
print(numeros)
print(f'Soma: {soma}')
print(f'Multiplicação: {mult}')
