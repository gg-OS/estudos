def teste(x):
    if x >= 0:
        print('Positivo')
    else:
        print('Negativo')


while True:
    n = float(input('Insira um número: '))
    teste(n)
    cont = input('\nDeseja continuar? (Sim/Não): ')
    if cont.title() == 'Sim':
        continue
    else:
        break
print()
print('powered by ggOS®')
