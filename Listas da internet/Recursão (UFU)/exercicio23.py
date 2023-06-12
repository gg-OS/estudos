def somatorio(v):
    if len(v) == 0:
        return 0
    else:
        n = v[0]
        del v[0]
        return n + somatorio(v)


vetor = [1, 2, 3, 4, 5, 6]

print(f'Somatorio do vetor = {somatorio(vetor)}')

print()
print('powered by ggOS')
