from math import floor


def multiplicacao_russa(a, b):
    if a == 1:
        return b
    else:
        if a % 2 == 0:
            return multiplicacao_russa(floor(a/2), b*2)
        else:
            return multiplicacao_russa(floor(a/2), b*2) + b


a_ = input('Insira o número A: ')
b_ = input('Insira o número B: ')

try:

    a_ = int(a_)
    b_ = int(b_)
    resultado = multiplicacao_russa(a_, b_)
    print(f'Multiplicação Russa({a_}, {b_}) = {resultado}')

except ValueError:

    print('Números inválidos. Encerrando programa...')

print()
print('powered by ggOS')
