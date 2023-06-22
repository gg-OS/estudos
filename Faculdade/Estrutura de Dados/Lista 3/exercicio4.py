while True:
    palavra = input('Insira uma palavra de 10 caracteres: ')
    if len(palavra) != 10:
        continue
    else:
        break
pv = []
cont = len(palavra)
for letra in palavra:
    pv.append(letra)
    if letra in ['a', 'e', 'i', 'o', 'u']:
        cont -= 1
print(pv)
print(f'Número de consoantes: {cont}')
