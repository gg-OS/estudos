lista = []
n = 0
while n < 10:
    numero = input('Insira um número inteiro: ')
    if not numero.isnumeric():
        continue
    else:
        n += 1
        lista.insert(0, numero)
print(lista)
print()
print('Fim do programa')
