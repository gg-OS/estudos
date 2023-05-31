class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade <= 21:
            self.altura += 1
        self.idade += 1
        print(f'Agora seu personagem possui {self.idade} anos.')
        return

    def engordar(self):
        self.peso += 1
        print(f'Peso atual = {self.peso}kg.')
        return

    def emagrecer(self):
        self.peso -= 1
        print(f'Peso atual = {self.peso}kg.')
        return

    def crescer(self):
        self.altura += 1
        print(f'Altura atual = {self.altura}cm.')
        return

    def atributos(self):
        print(f'Nome = {self.nome}')
        print(f'Idade = {self.idade} anos.')
        print(f'Peso = {self.peso}kg.')
        print(f'Altura = {self.altura} m')


print('Simulador de pessoa!\n')
print('Agora, você deve inserir alguns dados sobre seu personagem!')
print('Qual o nome do seu personagem?')
nome = input('Nome: ')
print()
print('Qual a idade do seu personagem?')
idade = input('Idade: ')
idade = int(idade)
print()
print('Qual o peso de seu personagem?')
peso = input('Peso: ')
peso = float(peso)
print()
print('Qual a altura de seu personagem?')
altura = input('Altura: ')
altura = float(altura)
print()

print('Menu de ações:\n'
      '1 - Envelhecer (1 ano)\n'
      '2 - Engordar (1 kg)\n'
      '3 - Emagrecer (1 kg)\n'
      '4 - Crescer (1 cm)\n'
      '5 - Visualizar atributos\n'
      '0 - Encerrar')
print()

personagem = Pessoa(nome, idade, peso, altura)

while True:
    acao = input('Insira uma ação: ')

    if acao == '1':
        personagem.envelhecer()

    elif acao == '2':
        personagem.engordar()

    elif acao == '3':
        personagem.emagrecer()

    elif acao == '4':
        personagem.crescer()

    elif acao == '5':
        personagem.atributos()

    elif acao == '0':
        print('Encerrando personagem')
        break

    else:
        print('Ação inválida')
        continue

print('powered by ggOS')
