pop_a = 80000
pop_b = 200000
y = 0
while True:
    c_a = input('Informe a taxa de crescimento da cidade A: ')
    c_b = input('Informe a taxa de crescimento da cidade B: ')
    if c_a.replace('.', '').isdigit() and c_b.replace('.', '').isdigit():
        c_a = 1 + (float(c_a) / 100)
        c_b = 1 + (float(c_b) / 100)
        break
    else:
        print('Uma das taxas inseridas é inválida, por favor insira novamente.')
        continue
while pop_b > pop_a:
    pop_a = pop_a * c_a
    pop_b = pop_b * c_b
    y += 1
print(f'A cidade A atingirá a população da cidade B em {y} anos.')
