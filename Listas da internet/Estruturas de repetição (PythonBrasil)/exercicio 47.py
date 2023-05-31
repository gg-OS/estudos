j = 1
soma = 0
maior = 0
menor = 0
nome = input('Insira o nome do atleta: ')
while j <= 7:
    nota = input(f'Nota do jurado #{j}: ')
    nota = float(nota)
    if j == 1:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
    soma += nota
    j += 1
media = soma/j
print()
print('Resultado final')
print('---------------')
print(f'Atleta: {nome}')
print(f'Melhor nota: {maior}')
print(f'Pior nota: {menor}')
print(f'Média: {media:.1f}')
print()
print('Torneio de verão do LAVROV')
