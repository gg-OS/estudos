"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
lula = 0
bolsonaro = 0
ciro = 0
cont = 0
while True:
    eleitores = input('Insira o número de eleitores: ')
    if not eleitores.isnumeric():
        print('Insira apenas números inteiros.')
        continue
    else:
        eleitores = int(eleitores)
        break
while cont <= eleitores:
    voto = input('Escolha seu candidato: ')
    if voto == '13':
        lula += 1
    elif voto == '22':
        bolsonaro += 1
    elif voto == '12':
        ciro += 1
    else:
        print('Voto inválido.')
        cont -= 1
    cont += 1
print(f'Lula: {lula}')
print(f'Bolsonaro: {bolsonaro}')
print(f'Ciro: {ciro}')