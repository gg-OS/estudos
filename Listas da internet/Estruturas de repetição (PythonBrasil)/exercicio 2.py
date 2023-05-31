x = 0
usuario = 'lavrov'
senha = 'chicao'
while x != 1:
    user = input('Usuário: ')
    key = input('Senha: ')
    if user != usuario and key != senha:
        print('Usuário ou senha inválidos.')
    else:
        print('Você está logado.')
        x += 1
