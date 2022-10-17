sexo = input('Qual seu sexo?: ')
altura = input('Qual sua altura em cm?: ')
peso_ideal = 0
if not altura.isnumeric():
    print('Por favor insira corretamente sua altura.')
else:
    altura = int(altura) / 100
    if sexo == 'masculino':
        peso_ideal = (72.7 * altura) - 58
    if sexo == 'feminino':
        peso_ideal = (62.1 * altura) - 44.7
print(f'O peso ideal recomendado na altura de {altura:.2f} para o sexo {sexo} é de {peso_ideal:.2f}')
