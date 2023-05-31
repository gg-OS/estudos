numero = input('Insira um número inteiro: ')
if numero.isdigit() and numero != '0':
    numero = int(numero)
    resto = numero % 2
    if resto == 0:
        print('Número par')
    else:
        print('Número ímpar')
else:
    print('Insira apenas números inteiros.')
