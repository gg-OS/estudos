soma = 0
n = input('Insira um número: ')
n = int(n)
for i in range(1, n + 1):
    soma += (1 / i)
print(f'Soma = {soma:.4f}')
print()
print('powered by ggOS')
