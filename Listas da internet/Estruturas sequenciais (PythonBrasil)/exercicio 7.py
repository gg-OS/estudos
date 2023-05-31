lado = input('Por favor insira o tamanho do lado do quadrado: ')
if not lado.isnumeric():
    print('Por favor insira apenas um número inteiro')
else:
    lado = int(lado)
    quadrado = lado ** 2
    print(f'O dobro da área do quadrado vale: {quadrado * 2}')
