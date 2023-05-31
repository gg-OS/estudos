x = 0
maior = 0
menor = 0
soma = 0
while True:
    n = input('Quantos numeros termos no conjunto? ')
    if not n.isnumeric():
        print('Insira um número inteiro.')
        continue
    n = int(n)
    while x < n:
        numero = input('Insira um numero: ')

        if not numero.isnumeric():
            print('Insira apenas números inteiros.')
            continue
        elif x == 0:
            numero = int(numero)
            menor = numero
            x += 1
        else:
            numero = int(numero)
            if numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero
            soma += numero
            x += 1
    break
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A soma dos números é: {soma}')
