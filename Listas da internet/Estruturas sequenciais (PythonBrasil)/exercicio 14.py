peso = input('Qual o peso do peixe? ')
peso = float(peso)
excesso = peso - 50
multa = excesso * 4
if excesso <= 0:
    print('Você não pagará multa!')
else:
    print(f'A multa a ser paga será de: {multa:.2f}')
