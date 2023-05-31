a = 0
n = 0
soma = 0
bons = 0
media = []
while a < 10:
    soma = 0
    n = 0
    while n < 4:
        nota = input(f'Insira a nota #{n + 1}: ')
        if nota.replace('.', '').isnumeric():
            nota = float(nota)
            if nota > 10 or nota < 0:
                print('Nota inválida.')
                continue
            soma += nota
            n += 1
        else:
            print('Nota inválida.')
            continue
    media.append(soma / n)
    a += 1
for aluno in media:
    if aluno >= 7:
        bons += 1
print(media)
print(bons)