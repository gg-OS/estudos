def somaserie(i, j, k):
    if i >= j:
        return 0

    else:
        return i + somaserie(i + k, j, k)


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
            resultado = somaserie(inicio, fim, incremento)

    elif fim < inicio:

        if incremento <= 0:
            print('Incremento menor que zero ou igual a zero.')
        else:
            resultado = somaserie(fim, inicio, incremento)
    else:
        resultado = fim

    print(f'Resultado = {resultado}')

except ValueError:
    print('Você fez alguma coisa errada;\n')

print()
print('powered by ggOS')
