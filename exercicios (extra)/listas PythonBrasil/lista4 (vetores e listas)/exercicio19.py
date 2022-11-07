sistemas = []
soma = 0
for i in range(0, 6):
    s = input(f'Votos do sistema #{i + 1}: ')
    while not s.isnumeric():
        print('Voto inválido.')
        s = input(f'Votos do sistema #{i + 1}: ')
    s = int(s)
    sistemas.append(s)
    soma += s
print('Sistema Operacional\tVotos\t%')
print('------------------\t-----\t---')
print(f'Windows Server:\t{sistemas[0]}\t{(sistemas[0] / soma) * 100:.0f}%')
print(f'Unix:\t\t\t{sistemas[1]}\t{(sistemas[1] / soma) * 100:.0f}%')
print(f'Linux:\t\t\t{sistemas[2]}\t{(sistemas[2] / soma) * 100:.0f}%')
print(f'Netware:\t\t{sistemas[3]}\t\t{(sistemas[3] / soma) * 100:.0f}%')
print(f'Mac OS:\t\t\t{sistemas[4]}\t\t{(sistemas[4] / soma) * 100:.0f}%')
print(f'Outros:\t\t\t{sistemas[5]}\t\t{(sistemas[5] / soma) * 100:.0f}%')
print()
print('Powered by ggOS')
