# Jogo de Craps
import random


def sorte():
    num = random.randint(2, 12)
    return num


input('Pressione qualquer tecla para iniciar.')
n = sorte()
if n == 7 or n == 11:
    print(f'Você tirou {n}!')
    print('Você é um natural!')
    print('Você venceu!')
elif n == 2 or n == 3 or n == 12:
    print(f'Você tirou {n}!')
    print('C R A P S')
    print('Você perdeu!')
else:
    print(f'Você tirou {n}, esse é o seu ponto!')
    input('Pressione qualquer tecla para próxima jogada.')
    print()
    valor = n
    while True:
        n = sorte()
        if n == 7:
            print(f'Você tirou {n}!')
            print('C R A P S')
            print('Você perdeu!')
            break
        elif n == valor:
            print(f'Você tirou {n}!')
            print('R E C E B A')
            print('Você venceu!')
            break
        else:
            print(f'Você tirou {n}!')
            print()
            input('Pressione qualquer tecla para próxima jogada.')
