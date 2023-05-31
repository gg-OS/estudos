def valorimposto(v, d):
    if d > 0:
        v = 1.03 * v + (v * (0.001 * d))
    return v


total = []
p = 0
while True:
    valor = input('Insira o valor da prestação: ')
    if valor == '0' or not valor.isnumeric():
        break
    elif not valor.isnumeric():
        print('Valor inválido.')
        print()
        continue
    else:
        valor = float(valor)
    dias = input('Insira quantos dias está em atraso: ')
    if not dias.isnumeric():
        print('Valor inválido.')
        print()
    else:
        dias = int(dias)
    total.append(valorimposto(valor, dias))
    p += 1

print()
print(f'Número de prestações pagas: {p}')
print(f'O valor total pago em prestações é: R$ {sum(total):.2f}')
