c = 0
maior = 0
while True:
    nota = input('Insira a média do aluno: ')
    nota = float(nota)
    if c == 0:
        maior = nota
        c += 1
    else:
        if maior < nota:
            maior = nota
    continuar = input('Deseja continuar? (S/N)')
    if continuar.title() == 'N':
        break
print(f'A maior média da turma foi {maior}')
