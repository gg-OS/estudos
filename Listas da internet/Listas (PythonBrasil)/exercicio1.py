lista = []
n = 0
while n < 5:
    numero = input('Insira um número inteiro: ')
    if not numero.isnumeric():
        continue
    else:
        lista.append(numero)
        n += 1
print(lista)
print()
print('Fim do programa')