def multiplicador(n1, n2):

    if n2 == 1:
        return n1

    return n1 + multiplicador(n1, n2 - 1)


num1 = input('Insira n1: ')
num2 = input('Insira n2: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f'n1 * n2 = {multiplicador(num1, num2)}\n')
except ValueError:
    print('Números inválidos, encerrando programa.\n')

print('powered by ggOS')