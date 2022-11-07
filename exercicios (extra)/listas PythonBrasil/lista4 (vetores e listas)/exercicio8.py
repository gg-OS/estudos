idades = []
alturas = []
c = 0

while c < 5:
    idade = input('Insira sua idade: ')
    while not idade.isnumeric():
        print('Insira uma idade válida.')
        print()
        idade = input('Insira sua idade: ')
    idade = int(idade)
    altura = input('Insira sua altura: ')
    while not altura.replace('.', '').isnumeric():
        print('Insira uma altura válida.')
        print()
        altura = input('Insira sua altura: ')
    altura = float(altura)
    alturas.insert(0, altura)
    idades.insert(0, idade)
    c += 1
print(idades)
print(alturas)
