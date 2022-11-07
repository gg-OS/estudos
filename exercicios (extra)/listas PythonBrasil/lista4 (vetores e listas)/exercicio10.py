v1 = []
v2 = []
v3 = []
c1 = 0
c2 = 0
c3 = 0
while c1 < 10:
    elem = input('Insira qualquer coisa: ')
    v1.append(elem)
    c1 += 1
while c2 < 10:
    elem = input('Insira qualquer coisa parte 2: ')
    v2.append(elem)
    c2 += 1
while c3 < 10:
    v3.append(v1[c3])
    v3.append(v2[c3])
    c3 += 1
print(v1)
print(v2)
print(v3)
