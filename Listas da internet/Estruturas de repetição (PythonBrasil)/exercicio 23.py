"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
x = 1
y = 1
cont = 1
resultado = '['
n = input('Insira um número: ')
if n.isnumeric():
    n = int(n)
    while x < n:
        if x == 1:
            resultado += str(x) + ',' + ' '
            x += 1
        else:
            while y < x:
                if x % y == 0:
                    cont += 1
                y += 1
            if cont == 2:
                resultado += str(x) + ',' + ' '
            x += 1
            cont = 1
            y = 1
resultado = resultado[:-2] + ']'
print(resultado)
