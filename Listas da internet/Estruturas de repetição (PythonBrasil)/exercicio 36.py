resultado = ''
while True:
    numero = input('Insira um número: ')
    menor = input('Começar por: ')
    maior = input('Terminar em: ')
    if numero.isnumeric() and maior.isnumeric() and menor.isnumeric():
        numero = int(numero)
        maior = int(maior)
        menor = int(menor)
        if maior <= menor:
            print('Dados inválidos')
            continue
        else:
            break
    else:
        print('Insira um número inteiro.')
        continue
while menor <= maior:
    res = numero * menor
    print(f'{numero} x {menor} = {res}')
    menor += 1
    