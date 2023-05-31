nome = input('Insira seu nome: ')
novo = ''
for l in range(1, len(nome) + 1):
    novo += nome[-l]
print(novo.upper())
