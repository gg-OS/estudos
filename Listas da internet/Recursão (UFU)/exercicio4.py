def potencia(k, n):

    if n == 1:
        return k

    return k * potencia(k, n - 1)


k_ = input('Insira k: ')
n_ = input('Insira n: ')

try:
    k_ = int(k_)
    n_ = int(n_)
    print(f'k^n = {potencia(k_, n_)}\n')
except ValueError:
    print('Números inválidos, encerrando programa.\n')

print('powered by ggOS')
