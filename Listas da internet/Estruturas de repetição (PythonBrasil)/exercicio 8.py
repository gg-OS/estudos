x = 0
soma = 0
media = 0
while x < 5:
    numero = input('Insira um número inteiro: ')
    if not numero.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        numero = int(numero)
        soma = soma + numero
        x += 1
media = soma / x
print(f'A soma dos números é {soma} e a média é {media:.2f}.')
