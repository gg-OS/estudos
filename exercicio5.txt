x = input('Insira o número da base: ')
x = float(x)
n = input('Insira a potência: ')
if not n.isnumeric():
    print('Apenas números inteiros são válidos.')
else:
    n = int(n)
    if n <= 1:
        print('O valor da potência deve ser maior que 1')
    else:
        resultado = x ** n
        print()
        print(f'Resultado = {resultado}')
print()
print('powered by ggOS')
