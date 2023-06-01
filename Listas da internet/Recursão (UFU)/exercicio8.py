def impressora(n):
    if n == 0:
        print(n)
        return

    else:
        print(n)
        return impressora(n - 1)


print('Algoritmo para imprimir todos os números de 0 a N em ordem decrescente.\n')

numero = input('Insira o número N: ')

try:
    numero = int(numero)
    impressora(numero)
except ValueError:
    print('Número inválido. Encerrando programa...\n')

print('powered by ggOS')
