b22 = 0
l13 = 0
c12 = 0
f30 = 0
nulo = 0
print('Eleições 2022')
while True:
    print('Candidatos: Bolsonaro - 22\nLula - 13\nCiro - 12\nÁvila - 30\nNulo - 0\n99 - Fechar aplicação')
    print()
    voto = input('Qual seu voto? ')
    if voto.isnumeric():
        if voto == '22':
            b22 += 1
        elif voto == '13':
            l13 += 1
        elif voto == '12':
            c12 += 1
        elif voto == '30':
            f30 += 1
        elif voto == '0':
            nulo += 1
        elif voto == '99':
            break
        else:
            print('Voto inválido.')
            continue
    else:
        continue
print(f'Bolsonaro - {b22} votos')
print(f'Lula - {l13} votos')
print(f'Ciro - {c12} votos')
print(f'Felipe Davila - {f30} votos')
print(f'Nulos - {nulo} votos')
print()
print('"Que Deus tenha misericórida dessa nação"')
