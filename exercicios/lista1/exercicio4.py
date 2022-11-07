fat = 1
num = input('Insira o número a calcular o fatorial: ')
if not num.isnumeric():
    print('Caractere inválido')
else:
    num = int(num)
    if num <= 0:
        print('Inválido: menor ou igual a zero')
    else:
        for i in range(num, 0, -1):
            fat = fat * i
print()
print(f'Resultado: !{num} = {fat}')
print()
print('powered by ggOS®')
