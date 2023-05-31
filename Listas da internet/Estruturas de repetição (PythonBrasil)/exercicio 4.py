pop_a = 80000
pop_b = 200000
c_a = 1.03
c_b = 1.015
y = 0
while pop_b > pop_a:
    pop_a = pop_a * c_a
    pop_b = pop_b * c_b
    y += 1
print(y)
