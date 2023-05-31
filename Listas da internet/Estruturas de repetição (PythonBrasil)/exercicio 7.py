x = 0
maior = 0
while x < 5:
    numero = input('Insira um número inteiro: ')
    if not numero.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        numero = int(numero)
        if numero > maior:
            maior = numero
        x += 1
print(f'O maior número é {maior}.')
