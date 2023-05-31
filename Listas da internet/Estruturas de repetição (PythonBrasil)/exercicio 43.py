nota = ''
total = 0
while True:
    codigo = input('Insira o código do produto: ')
    qtd = input('Insira a quantidade: ')
    if not qtd.isnumeric():
        continue
    qtd = int(qtd)
    if codigo == '100':
        total += 1.20 * qtd
        nota += '(+) Cachorro Quente R$ 1.20\n'
    elif codigo == '101':
        total += 1.30 * qtd
        nota += '(+) Bauru Simples R$ 1.30\n'
    elif codigo == '102':
        total += 1.50 * qtd
        nota += '(+) Bauru com ovo R$ 1.50\n'
    elif codigo == '103':
        total += 1.20 * qtd
        nota += '(+) Hambúrguer R$ 1.20\n'
    elif codigo == '104':
        total += 1.30 * qtd
        nota += '(+) Cheeseburguer R$ 1.30\n'
    elif codigo == '105':
        total += 1.00 * qtd
        nota += '(+) Refrigerante R$ 1.00\n'
    else:
        break
print(nota)
print(f'Total: R$ {total:.2f}')
