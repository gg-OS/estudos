print('Comparativo de consumo de combustível\n')
carros = []
consumos = []
c = 0
m = 0
menor = ''
while c < 5:
    print(f'Veículo #{c + 1}')
    carro = input('Nome: ').title()
    carros.append(carro)
    consumo = input('Km por litro: ')
    print()
    if not consumo.replace('.', '').isnumeric():
        continue
    else:
        consumo = float(consumo)
        consumos.append(consumo)
        c += 1
    if c == 1:
        menor = carro
        m = consumo
    else:
        if consumo > m:
            m = consumo
            menor = carro
for n in range(0, c):
    mil = 1000 / consumos[n]
    valor = mil * 2.25
    print(f'{n + 1} - {carros[n]} - {consumos[n]:.1f} km/l - {mil:.2f} litros - R$ {valor:.2f} ')
print(f'\nO veículo de menor consumo é o {menor}.')
print()
print('Powered by ggOS')
