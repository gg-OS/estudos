def inversor(v, inicio, fim):
    if inicio >= fim:
        return

    v[inicio], v[fim] = v[fim], v[inicio]
    return inversor(v, inicio + 1, fim - 1)


vetor = []
for i in range(0, 100):
    vetor.append(i)

inversor(vetor, 0, len(vetor) - 1)

print(vetor)

print('powered by ggOS')
