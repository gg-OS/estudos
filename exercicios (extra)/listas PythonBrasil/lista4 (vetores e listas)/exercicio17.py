saltos = []
soma = 0
n = 0

while True:
    nome = input('Insira o nome do atleta: ')
    if nome.isnumeric():
        print('Nome inválido')
        continue
    else:
        while n < 5:
            salto = input(f'Insira a altura do salto #{n + 1}: ')
            if salto.replace('.', '').isnumeric():
                salto = float(salto)
                saltos.append(salto)
                soma += salto
                n += 1
            else:
                print('Altura inválida.')
                print()
        break
media = soma / n
print()
print(f'Atleta: {nome}')
print()
print(f'Primeiro Salto: {saltos[0]:.1f} m')
print(f'Segundo Salto: {saltos[1]:.1f} m')
print(f'Terceiro Salto: {saltos[2]:.1f} m')
print(f'Quarto Salto: {saltos[3]:.1f} m')
print(f'Quinto Salto: {saltos[4]:.1f} m')
print()
print(f'Resultado Final:\nAtleta: {nome}\nSaltos: {saltos}\nMédia dos resultados: {media:.1f} m')
print()
print('Powered by ggOS')