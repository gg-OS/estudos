while True:
    nota = input('Insira uma nota de 0 a 10: ')
    if not nota.isnumeric():
        print('Por favor insira apenas números inteiros')
    else:
        nota = int(nota)
        if nota > 10:
            print('Por favor insira valores entre 0 e 10.')
        else:
            print(f'Nota: {nota}')
            break
