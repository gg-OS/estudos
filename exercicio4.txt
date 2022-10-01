c = 0
soma = 0
while True:
    idade = input(f'Insira a idade do indivíduo {c + 1}: ')
    if not idade.replace('-', '').isnumeric():
        print('Idade inválida')
        continue
    idade = int(idade)
    if idade < 0:
        break
    soma += idade
    c += 1
print()
print(f'Média de idade do grupo = {soma / c:.1f}')
print()
print('powered by ggOS')
