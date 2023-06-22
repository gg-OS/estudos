v1 = []
v2 = []
v3 = []
v4 = []
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while c1 < 10:
    elem = input('Insira qualquer coisa: ')
    v1.append(elem)
    c1 += 1
while c2 < 10:
    elem = input('Insira qualquer coisa parte 2: ')
    v2.append(elem)
    c2 += 1
while c3 < 10:
    elem = input('Insira qualquer coisa parte 3: ')
    v3.append(elem)
    c3 += 1
while c4 < 10:
    v4.append(v1[c4])
    v4.append(v2[c4])
    v4.append(v3[c4])
    c4 += 1
print(v1)
print(v2)
print(v3)
print(v4)
