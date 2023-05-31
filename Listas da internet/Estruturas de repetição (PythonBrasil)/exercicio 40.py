"""
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999)
"""
"""
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
x = 0
maior = 0
menor = 0
media = 0
c2k = 0
media_2k = 0
media_v = 0
c_maior = ''
c_menor = ''
while x < 5:
    cidade = input('Insira o nome da cidade: ')
    nvp = input('Insira o número de veículos de passeio: ')
    while not nvp.isnumeric():
        print('Dado inválido.')
        print()
        nvp = input('Insira o número de veículos de passeio: ')
    nvp = int(nvp)
    nat = input('Insira a quantidade de acidentes com vítimas: ')
    while not nat.isnumeric():
        print('Dado inválido.')
        print()
        nat = input('Insira a quantidade de acidentes com vítimas: ')
    nat = int(nat)
    if x == 0:
        maior = nat
        menor = nat
    if maior < nat:
        maior = nat
        c_maior = cidade
    elif menor > nat:
        menor = nat
        c_menor = cidade
    else:
        if nvp > 2000:
            media_2k += nat
            c2k += 1
        media += nat
        media_v += nvp
    x += 1
print(f'Média de acidentes: {media / x}')
print(f'Média de veículos de passeio: {media_v / x}')
print(f'Cidade mais perigosa: {c_maior} - {maior} acidentes')
print(f'Cidade mais segura: {c_menor} - {menor} acidentes')
print(f'Média de acidentes em cidades pequenas: {media_2k / c2k}')
