temperatura = input('Insira a temperatura que deseja converter: ')
temperatura = float(temperatura)
temperatura = 5 * ((temperatura - 32) / 9)
print(f'A temperatura informada equivale a {temperatura:.1f} graus Celcius.')
