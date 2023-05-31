frase = input('Insira uma frase a ser convertida para leet: ')
if 'e' in frase.lower():
    frase = frase.replace('e', '3')
if 't' in frase.lower():
    frase = frase.replace('t', '7')
if 'a' in frase.lower():
    frase = frase.replace('a', '4')
if 'o' in frase.lower():
    frase = frase.replace('o', '0')
print(frase)
print()
print('powered by ggOS')
