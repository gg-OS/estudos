letra = input('Por favor insira uma letra: ')
if letra.isnumeric():
    print('LETRA')
letra = letra.lower()
if not letra in ('a', 'e', 'i', 'o', 'u'):
    print('Consoante')
else:
    print('Vogal')
