cont = 0
r1 = input('Telefonou para a vítima? ')
if r1.title() == 'Sim':
    cont += 1
r2 = input('Esteve no local do crime? ')
if r2.title() == 'Sim':
    cont += 1
r3 = input('Mora perto da vítima? ')
if r3.title() == 'Sim':
    cont += 1
r4 = input('Devia para a vítima? ')
if r4.title() == 'Sim':
    cont += 1
r5 = input('Já trabalhou com a vítima? ')
print()
if r5.title() == 'Sim':
    cont += 1
if cont == 5:
    print('Assassino')
elif 3 <= cont <= 4:
    print('Cúmplice')
elif cont == 2:
    print('Suspeito')
else:
    print('Inocente')
