n1 = input('Insira sua primeira nota: ')
if not n1.replace('.', '').isnumeric():
    print('Por favor insira apenas números.')
else:
    n1 = float(n1)
n2 = input('Insira sua segunda nota: ')
if not n2.replace('.', '').isnumeric():
    print('Por favor insira apenas números.')
else:
    n2 = float(n2)
media = (n1 + n2) / 2
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7.0 and media != 10:
    print('Aprovado')
else:
    print('Reprovado')