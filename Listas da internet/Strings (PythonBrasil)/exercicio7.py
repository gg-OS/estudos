frase = input('Digite uma frase: ')
espaco = 0
vogal = 0
for i in range(0, len(frase)):
    if frase[i] == ' ':
        espaco += 1
    elif frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        vogal += 1
print()
print(f'Número de espaços: {espaco}')
print(f'Número de vogais: {vogal}')
