nome = input('Insira seu nome: ')
for l in range(0, len(nome)):
    print(nome[:l + 1].upper())
