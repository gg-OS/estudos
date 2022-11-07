string_1 = input('Insira a primeira string: ')
string_2 = input('Insira a segunda string: ')

print(f'String 1: {string_1}')
print(f'String 2: {string_2}')
print(f'Tamanho de {string_1}: {len(string_1)} caracteres')
print(f'Tamanho de {string_2}: {len(string_2)} caracteres')

if len(string_1) == len(string_2):
    print('Strings de tamanhos iguais.')
if string_1 == string_2:
    print('As strings são iguais no conteúdo.')

