resultado = ''
while True:
    salto = 1
    maior = 0
    menor = 0
    soma = 0
    nome = input('Insira o nome do atleta: ')
    if nome.title() == 'Fim':
        break
    while salto <= 5:
        nota = input(f'Salto #{salto}: ')
        nota = float(nota)
        if salto == 1:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            elif nota < menor:
                menor = nota
        soma += nota
        salto += 1
    soma = soma - maior - menor
    media = soma/(salto - 3)
    resultado += nome + ':' + ' ' + str(f'{media:.1f}') + ' ' + 'm' + '\n'
    print(f'Atleta: {nome}')
    print()
    print(f'Melhor salto: {maior} m')
    print(f'Pior salto: {menor} m')
    print(f'Média dos demais saltos: {media:.1f} m')
    print()
print()
print('Resultado final:')
print(resultado)
print()
print('Torneio de verão do LAVROV')
