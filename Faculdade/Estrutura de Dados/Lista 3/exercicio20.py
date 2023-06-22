salarios = []
abonos = []
f = 0
m = 0
maior = 0

while True:
    salario = input(f'Insira o salário do funcionário #{f + 1}: ')
    if not salario.replace('.', '').isnumeric():
        print('Salário inválido.\n')
        continue
    else:
        salario = float(salario)
    if salario == 0:
        break
    if (salario * 0.2) < 100:
        abono = 100
        m += 1
    else:
        abono = (salario * 0.2)
        if abono > maior:
            maior = abono
    f += 1
    salarios.append(salario)
    abonos.append(abono)
print('\nSalário - Abono')
for n in range(0, f):
    print(f'R$ {salarios[n]} - R$ {abonos[n]:.2f}')

print()
print(f'Foram processados {f} colaboradores.')
print(f'Total gasto com abonos: R$ {sum(abonos):.2f}')
print(f'Valor mínimo pago a {m} colaboradores')
print(f'Maior valor de abono pago: R$ {maior}')
print()
print('Powered by ggOS')
