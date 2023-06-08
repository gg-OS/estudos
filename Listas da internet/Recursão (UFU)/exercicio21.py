def sequencia(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (2 * sequencia(n - 1)) + (3 * sequencia(n - 2))


numero = input('Insira um número para calcular a sequência do exercício 21: ')

try:
    numero = int(numero)
    resultado = sequencia(numero)
    print(f'Sequencia = {resultado}')
except ValueError:
    print('Número inválido. Encerrando programa...')

print('powered by ggOS')
