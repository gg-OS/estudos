frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')
c = 0
for i in range(0, len(frase)):
    if frase[i] == frase[-i - 1]:
        c += 1

if c == len(frase):
    print('Palíndroma')
else:
    print('MPNSM')
