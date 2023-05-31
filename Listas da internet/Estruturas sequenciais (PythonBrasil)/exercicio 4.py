c = 1
m = 0
while c <= 4:
    nota = int(input(f'Insira a nota do {c} bimestre: '))
    m += nota
    c += 1
m = m / 4
print(f'A média do aluno foi de {m}')
