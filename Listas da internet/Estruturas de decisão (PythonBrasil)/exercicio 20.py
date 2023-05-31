nota1 = input('Insira a nota #1: ')
nota2 = input('Insira a nota #2: ')
nota3 = input('Insira a nota #3: ')
if not nota1.replace('.', '').isnumeric() or not nota2.replace('.', '').isnumeric() \
        or not nota3.replace('.', '').isnumeric():
    print('Por favor insira apenas números.')
else:
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    media = (nota1 + nota2 + nota3) / 3
    if media > 10:
        print('Valores inválidos de notas')
    elif media == 10:
        print('Aprovado com distinção')
    elif 7.0 <= media < 10:
        print('Aprovado')
    else:
        print('Reprovado')
