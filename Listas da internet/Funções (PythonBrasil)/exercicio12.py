import random


def embaralhar(palavra):
    nova = ''
    lista = list(palavra)
    while len(lista) > 0:
        x = random.randint(0, len(lista) - 1)
        nova += lista[x]
        del(lista[x])
    return nova


p = input('Insira uma palavra: ')
print(embaralhar(p))
print()
print('powered by ggOS®')