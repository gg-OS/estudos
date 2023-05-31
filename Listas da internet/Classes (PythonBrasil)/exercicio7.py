class Tamagushi:

    def __init__(self, n, i):
        self.nome = n
        self.fome = 10
        self.saude = 10
        self.idade = i
        self.humor = (self.fome + self.saude) / 2

    def alterar_nome(self, n):
        self.nome = n
        print(f'Feito! O novo nome do seu bichinho é {self.nome}')
        return

    def alterar_fome(self, var):
        if var is True:
            if var != 10:
                self.fome += 1
        else:
            self.fome -= 1
        return

    def alterar_saude(self, var):
        if var is True:
            if var != 10:
                self.saude += 1
        else:
            self.saude -= 1
        return

    def alterar_idade(self):
        self.idade += 1
        return

    def retornar_atributos(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Fome: {10 - self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'Humor: {(self.fome + self.saude) / 2}')


print('Tamagushi!')
print()
nome = input('Insira o nome do seu bichinho: ')
idade = input('Insira a idade do seu bichinho: ')
idade = int(idade)
bicho = Tamagushi(nome, idade)
print()
print('Botões:\n'
      '1 - Alterar nome\n'
      '2 - Passar um turno\n'
      '3 - Visualizar atributos\n'
      '4 - Alimentar\n'
      '5 - Cuidar\n'
      '0 - Encerrar jogo\n')

while True:

    acao = int(input('Escolha uma ação: '))

    if acao == 1:
        nome = input('Insira o novo nome: ')
        bicho.alterar_nome(nome)

    elif acao == 2:
        comida = False
        cuidado = False
        bicho.alterar_fome(comida)
        bicho.alterar_saude(cuidado)
        bicho.alterar_idade()
        print('Turno jogado!\n')

    elif acao == 3:
        bicho.retornar_atributos()
        print()

    elif acao == 4:
        comida = True
        bicho.alterar_fome(comida)
        print('Alimentando...\n')

    elif acao == 5:
        cuidado = True
        bicho.alterar_saude(cuidado)
        print('Cuidando...\n')

    elif acao == 0:
        print('Encerrando o Tamagushi!')
        break

    else:
        print('Ação inválida')

print()
print('powered by ggOS')
