from math import floor


def verificador(n, d, c):
    if n / 10 < 1:
        return c
    else:
        if n % 10 == d:
            c += 1
        return verificador(floor(n / 10), d, c)


numero = input('Insira um número para verificar a ocorrência de dígitos: ')
digito = input('Insira o dígito que deseja verificar: ')

try:
    digito = int(digito)
    numero = int(numero)
    resultado = verificador(numero, digito, 0)
    print(f'O dígito {digito} foi encontrado {resultado} vezes.')
except ValueError:
    print('Parâmetros errados. Encerrando programa.')

print()
print('powered by ggOS')
