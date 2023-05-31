palavra_secreta = 'eduardomeskita'
palavra_nova = ''
e = 6
while True:
    if e == 0:
        print('Você perdeu!')
        break
    else:
        letra = input('Insira uma letra: ').lower()
        if len(letra) > 1:
            print('Insira apenas uma letra.')
            continue

