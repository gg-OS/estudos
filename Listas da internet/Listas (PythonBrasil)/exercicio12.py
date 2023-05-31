soma = 0
idades = []
alturas = []
a = 0
a2 = 0
cont = 0
while a < 5:
    idade = input('Insira sua idade: ')
    idade = int(idade)
    altura = input('Insira sua altura: ')
    altura = float(altura)
    soma += altura
    idades.append(idade)
    alturas.append(altura)
    a += 1
media = soma / a

while a2 < a:
    if idades[a2] >= 13 and alturas[a2] > media:
        cont += 1
    a2 += 1
print(f'A média de altura da sala é de : {media:.2f}')
print()
print(f'A quantidade de alunos maiores de 13 anos acima da média de altura é de : {cont}')
