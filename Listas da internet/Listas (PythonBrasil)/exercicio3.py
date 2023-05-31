notas = []
n = 0
soma = 0
while n < 4:
    nota = input('Insira uma nota: ')
    if nota.isnumeric():
        nota = int(nota)
        if nota > 10 or nota < 0:
            continue
        else:
            n += 1
            notas.append(nota)
            soma += nota
    else:
        continue
print(f'As notas foram: {notas}')
print()
print(f'A média das notas foi: {soma / n}')
