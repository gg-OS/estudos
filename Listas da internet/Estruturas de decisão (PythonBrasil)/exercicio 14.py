media = input('Insira sua média: ')
if media.replace('.', '').isnumeric():
    media = float(media)
    if media > 10 or media < 0:
        print('Média inválida.')
    elif 9.0 <= media <= 10.0:
        print('Conceito A')
        print()
        print('APROVADO')
    elif 7.5 <= media < 9.0:
        print('Conceito B')
        print()
        print('APROVADO')
    elif 6.0 <= media < 7.5:
        print('Conceito C')
        print()
        print('APROVADO')
    elif 4.0 < media < 6.0:
        print('Conceito D')
        print()
        print('REPROVADO')
    else:
        print('Conceito E')
        print()
        print('REPROVADO')
else:
    print('Por favor insira apenas números')