import random
palavra = 'armando'
chances = 2
nova_palavra = ''
palavra_l = list(palavra)
while len(palavra_l) != 0:
    n = random.randint(0, len(palavra_l) - 1)
    nova_palavra += palavra_l[n]
    palavra_l.pop(n)
print(f'A palavra é: {nova_palavra}')
while True:
    if chances == 0:
        print('Você perdeu!')
        break
    tentativa = input('Insira a palavra a ser adivinhada: ')
    if tentativa == palavra:
        print('ACERTOU!! Você venceu!')
        break
    else:
        print(f'Errou! Restam {chances - 1} tentativas.')
        chances -= 1
print()
print('powered by ggOS')
