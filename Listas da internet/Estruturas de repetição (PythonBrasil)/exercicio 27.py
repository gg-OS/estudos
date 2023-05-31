"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

"""
soma = 0
cont = 0
while True:
    turmas = input('Insira a quantidade de turmas: ')
    if not turmas.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        turmas = int(turmas)
        break
while cont < turmas:
    alunos = input(f'Insira a quantidade de alunos na turma {cont + 1}: ')
    if not alunos.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        alunos = int(alunos)
        if alunos > 40 or alunos < 0:
            print('O máximo de alunos por turma é de 40.')
            continue
        else:
            soma += alunos
            cont += 1

media = soma / cont
print(f'A quantidade média de alunos por turma é de: {media}')
