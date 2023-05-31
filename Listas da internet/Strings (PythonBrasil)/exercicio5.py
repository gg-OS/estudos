nome = input('Insira seu nome: ')
for l in range(len(nome), 0, -1):
    print(nome[:l].upper())

