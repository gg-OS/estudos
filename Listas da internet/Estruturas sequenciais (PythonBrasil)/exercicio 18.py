velocidade = input('Qual a velocidade da sua internet (em mbps)? ')
if not velocidade.isnumeric():
    print('Por favor insira a velocidade apenas números inteiros.')
else:
    velocidade = int(velocidade)
tamanho = input('Qual o tamanho do arquivo que deseja baixar (em MBs)? ')
if not tamanho.replace('.', '').isnumeric():
    print('Por favor insira o tamanho do arquivo em números.')
else:
    tamanho = float(tamanho)
tempo = tamanho / (velocidade * 60)
print(f'Para baixar o arquivo, serão necessários {tempo:.1f} minutos.')
