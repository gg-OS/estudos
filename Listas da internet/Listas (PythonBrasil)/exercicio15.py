acima = 0  # Para valores acima da média
sete = 0  # Para valores abaixo de sete
q = 0  # Quantidade de valores
valores = []
inversa = []
soma = 0

while True:
    nota = input('Insira uma nota: ')
    nota = float(nota)
    if nota == -1:
        break
    else:
        soma += nota
        q += 1
        valores.append(round(nota))
        inversa.insert(0, nota)
        if nota < 7:
            sete += 1
    print('Valor inserido.')
    print()
media = soma / q
for valor in valores:
    if valor > media:
        acima += 1
print(f'Foram lidos {q} valores.')
print(valores)
for inv in inversa:
    print(round(inv))
print(f'Total da soma dos valores: {soma}')
print(f'Média dos valores: {media:.2f}')
print(f'Valores abaixo de sete: {sete}')
print(f'Valores acima da média: {acima}')
print()
print('Siiiiii!!!')
