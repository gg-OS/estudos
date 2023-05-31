jogadores = []
voto = 'a'
maior = 0
melhor = 0
for i in range(1, 24):
    jogadores.append(0)
while True:
    voto = input('Insira o voto: ')
    if voto == '0':
        break
    elif voto.isnumeric():
        voto = int(voto)
        jogadores[voto - 1] += 1
    else:
        print('Voto inválido.\n')
        continue
soma = sum(jogadores)
print('\nFim da votação\n')
for i in range(0, 22):
    if jogadores[i] == 0:
        continue
    else:
        if jogadores[i] > maior:
            maior = jogadores[i]
            melhor = i + 1
        print(f'Jogador #{i + 1}: {jogadores[i]} votos ({(jogadores[i] / soma) * 100:.0f}%)')
print()
perc = (maior / soma) * 100
print(f'Destaque da partida: Jogador #{melhor} com {maior} votos, correspondendo a {perc:.0f}% dos votos.')
print()
print('Powered by ggOS')
