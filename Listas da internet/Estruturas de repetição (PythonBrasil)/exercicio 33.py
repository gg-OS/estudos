cont = 0
maior = 0
menor = 0
soma = 0
while True:
    q = input('Quantas temperaturas analisaremos? ')
    if q.isnumeric():
        q = int(q)
        break
    else:
        print('Insira um número inteiro.')
        continue
while cont < q:
    temperatura = input(f'Insira a temperatura nº{cont + 1} (em Kelvin): ')
    if temperatura.replace('.', '').isnumeric():
        temperatura = float(temperatura)
        soma += temperatura
        if cont == 0:
            menor = temperatura
            maior = temperatura
        if temperatura > maior:
            maior = temperatura
        elif temperatura < menor:
            menor = temperatura
        cont += 1
    else:
        print('Insira um número válido.')
        continue
print(f'A media das temperaturas é : {soma / cont:.1f}')
print(f'A maior temperatura foi de {maior:.1f} K')
print(f'A menor temperatura foi de {menor:.1f} K')
