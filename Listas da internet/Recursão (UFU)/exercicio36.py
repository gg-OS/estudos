def mdc(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    return mdc(y, x % y)


_x = input('Insira o número x: ')
_y = input('Insira o número y: ')

_x = int(_x)
_y = int(_y)

print(mdc(_x, _y))

print('\nggOS')
