mes = 0
temps = []
soma = 0
cont = 0
while mes < 12:
    temperatura = input(f'Insira a temperatura média do mês #{mes + 1}: ')
    temperatura = float(temperatura)
    temps.append(temperatura)
    soma += temperatura
    mes += 1
media = soma / mes
mes = 0
while mes < 12:
    if temps[mes] > media:
        print(f'Mês: {mes + 1} - Temperatura média: {temps[mes]}')
    mes += 1