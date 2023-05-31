x = 1
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while True:
    numero = input('Insira um número inteiro: ')
    numero = float(numero)
    if numero < 0:
        break
    elif 0 <= numero <= 25:
        c1 += 1
    elif 25 < numero <= 50:
        c2 += 1
    elif 50 < numero <= 75:
        c3 += 1
    elif 75 < numero <= 100:
        c4 += 1
    else:
        continue
print(f'[0-25] = {c1}')
print(f'[26-50] = {c2}')
print(f'[51-75] = {c3}')
print(f'[76-100] = {c4}')
