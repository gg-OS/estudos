def conversor(t):
    r = (t - 32) * 5/9
    return r


print('Bem vindo ao conversor de temperatura ggOS')
temp = input('Insira uma temperatura em °F: ')
temp = float(temp)
resposta = conversor(temp)
print(f'A temperatura em graus centígrados é de {resposta:.1f}°C')
print()
print('powered by ggOS®')
