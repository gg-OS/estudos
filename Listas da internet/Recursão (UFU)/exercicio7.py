def impressora(n, v):
    if v == 0:
        print(n - v)
        return

    else:
        print(n - v)
        return impressora(n, v - 1)


print('Algoritmo para imprimir todos os números de 0 a N em ordem crescente.\n')

numero = input('Insira o número N: ')

try:
    numero = int(numero)
    impressora(numero, numero)
except ValueError:
    print('Número inválido. Encerrando programa...\n')

print('powered by ggOS')
