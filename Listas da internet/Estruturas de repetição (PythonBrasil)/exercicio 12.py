x = 1
while True:
    numero = input('Por favor insira um número: ')
    if not numero.isdigit():
        print('Por favor insira um número inteiro.')
        continue
    else:
        numero = int(numero)
        break
while x <= 10:
    print(f'{numero} x {x} = {numero * x}')
    x += 1
print()
print('Fim do programa.')