elemento = []
cont = 0
p1 = input('Telefonou para a vítima? ')
p1 = p1.title()
elemento.append(p1)
p2 = input('Esteve no local do crime? ')
p2 = p2.title()
elemento.append(p2)
p3 = input('Mora perto da vítima? ')
p3 = p3.title()
elemento.append(p3)
p4 = input('Devia para a vítima? ')
p4 = p4.title()
elemento.append(p4)
p5 = input('Já trabalhou com a vítima? ')
p5 = p5.title()
elemento.append(p5)
print()
if elemento.count('Sim') == 5:
    print('Assassino')
elif 4 >= elemento.count('Sim') >= 3:
    print('Cúmplice')
elif elemento.count('Sim') == 2:
    print('Suspeito')
else:
    print('Inocente')
print()
print('Sistemas de detecção ggOS')