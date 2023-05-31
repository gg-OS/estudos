a = 0
x = 0
soma = 0
maior = 0
menor = 0
while True:
    nota = 0
    aluno = input('Insira o nome do aluno: ')
    a += 1
    q = 1
    r1 = input(f'Insira a resposta da questão {q}: ')
    if r1.upper() == 'A':
        nota += 1
    q += 1
    r2 = input(f'Insira a resposta da questão {q}: ')
    if r2.upper() == 'B':
        nota += 1
    q += 1
    r3 = input(f'Insira a resposta da questão {q}: ')
    if r3.upper() == 'C':
        nota += 1
    q += 1
    r4 = input(f'Insira a resposta da questão {q}: ')
    if r4.upper() == 'D':
        nota += 1
    q += 1
    r5 = input(f'Insira a resposta da questão {q}: ')
    if r5.upper() == 'E':
        nota += 1
    q += 1
    r6 = input(f'Insira a resposta da questão {q}: ')
    if r6.upper() == 'E':
        nota += 1
    q += 1
    r7 = input(f'Insira a resposta da questão {q}: ')
    if r7.upper() == 'D':
        nota += 1
    q += 1
    r8 = input(f'Insira a resposta da questão {q}: ')
    if r8.upper() == 'C':
        nota += 1
    q += 1
    r9 = input(f'Insira a resposta da questão {q}: ')
    if r9.upper() == 'B':
        nota += 1
    q += 1
    r10 = input(f'Insira a resposta da questão {q}: ')
    if r10.upper() == 'A':
        nota += 1
    if a == 1:
        maior = nota
        menor = nota
    elif nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    soma += nota
    while x != 1:
        finalizar = input('Deseja inserir a nota de outro aluno? (sim/não) ')
        if finalizar.title() == 'Sim':
            break
        elif finalizar.title() == 'Não':
            x += 1
        else:
            print('Sim ou não?')
            continue
    if x == 1:
        break
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Total de alunos: {a}')
print(f'Média da turma: {soma / a:.1f}')
