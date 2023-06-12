def funcao(m, n):
    if m == 1:
        return n + 1
    elif n == 1:
        return m + 1
    else:
        return funcao(m, n - 1) + funcao(m - 1, n)


n1 = input('Insira o número m: ')
n2 = input('Insira o número n: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    print(f'h(m, n) = {funcao(n1, n2)}')
except ValueError:
    print('Erro nos valores inseridos. Encerrando programa...')

print()
print('powered by ggOS')
