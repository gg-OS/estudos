def somaserie(i, j, k):
    if i > j:
        return 0

    else:
        print(i)
        return somaserie(i + k, j, k)


inicio = input('Insira o início da série: ')
fim = input('Insira o fim da série: ')
incremento = input('Insira o incremento: ')
resultado = 0

try:

    inicio = int(inicio)
    fim = int(fim)
    incremento = int(incremento)

    if fim > inicio:
        if incremento <= 0:
            print('Incremento menor que zero ou igual a zero.')
        else:
            somaserie(inicio, fim, incremento)

    elif fim < inicio:

        if incremento <= 0:
            print('Incremento menor que zero ou igual a zero.')
        else:
            somaserie(fim, inicio, incremento)
    else:

        print(fim)

except ValueError:

    print('Você fez alguma coisa errada;\n')

print()
print('powered by ggOS')
