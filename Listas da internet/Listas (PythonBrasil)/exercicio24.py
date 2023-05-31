import random
c = 0
dado = [0, 0, 0, 0, 0, 0]
while c < 100:
    x = random.randint(1, 6)
    dado[x - 1] += 1
    c += 1
for n in range(1, 7):
    print(f'O valor {n} apareceu {dado[n - 1]} vezes.')
