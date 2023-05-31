from random import randint


class Tamagushi:

    def __init__(self, name, age):
        self.nome = name
        self.fome = randint(0, 10)
        self.saude = randint(5, 10)
        self.idade = age * 52
        self.humor = randint(0, 10)

    def set_nome(self, name):
        self.nome = nome

    def set_fome(self, fome):
        self.fome = fome

    def set_humor(self, v):
        self.humor = v

    def set_saude(self, saude):
        self.saude = saude

    def set_idade(self, age):
        self.idade = idade * 52

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def get_porta(self):
        return self.nome, self.idade / 52, self.fome, self.saude, self.humor

    def brincar(self, tempo):
        self.humor += 1 * tempo
        self.fome -= 1 * tempo
        self.idade += tempo

    def alimentar(self, qtd):
        self.humor = (0.5 * qtd) + self.humor
        self.fome += 1 * qtd
        self.idade += qtd

    def agradecimento(self):
        print(f'{self.nome}: "waaaaaaaaa"')


def validador(age, t):
    if t == 'i':
        while True:
            try:
                age = int(age)
                return age
            except ValueError:
                print('Dados inválidos')
                age = input('Por favor insira apenas números inteiros: ')


bichos = []
selec = 0

print('Menu:\n'
      '1 - Criar um bichinho\n'
      '2 - Selecionar um bichinho\n'
      '3 - Alimentar o bichinho\n'
      '4 - Brincar com o bichinho\n'
      '5 - Alterar algum valor\n'
      '6 - Falar com o bichinho\n'
      '0 - Encerrar programa\n'
      'Ah... E existe um comando secreto...\n')

while True:

    acao = input('Selecione uma ação: ')

    if acao == '1':
        nome = input('Insira o nome do bichinho: ')
        idade = input('Insira a idade do bichinho: ')
        idade = validador(idade, 'i')
        bichos.append(Tamagushi(nome, idade))
        print(f'{nome} foi criado com sucesso!')

    elif acao == '2':

        if len(bichos) != 0:
            for i in range(len(bichos)):
                print(f'{i} | {bichos[i].get_nome()}')
            print('Algumas lendas dizem que se você digitar "hoohaa" acontece algo estranho...')
            selec = input('Selecione um bichinho pelo índice: ')
            if selec == 'hoohaa':
                print('Todos os bichos foram selecionados.')
            else:
                selec = validador(selec, 'i')
                print(f'{bichos[selec].get_nome()} foi selecionado.')

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '3':

        if len(bichos) != 0:
            if selec == 'hoohaa':
                for i in range(len(bichos)):
                    bichos[i].alimentar(1)
                    bichos[i].agradecimento()
                print('Você alimentou todos os bichos 1 vez.')

            else:
                turnos = input(f'Quantas vezes deseja alimentar {bichos[selec].get_nome()}? ')
                turnos = validador(turnos, 'i')
                if turnos > 3:
                    turnos = 3
                    print('O máximo são 3 turnos')
                bichos[selec].alimentar(turnos)
                print(f'Você alimentou {bichos[selec].get_nome()} {turnos} vezes.')

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '4':

        if len(bichos) != 0:
            if selec == 'hoohaa':
                for i in range(len(bichos)):
                    bichos[i].brincar(1)
                print('Você brincou com todos os bichos por 1 turno.')

            else:
                turnos = input(f'Quantas vezes deseja brincar com {bichos[selec].get_nome()}? ')
                turnos = validador(turnos, 'i')
                if turnos > 3:
                    turnos = 3
                    print('O máximo são 3 turnos')
                bichos[selec].brincar(turnos)
                print(f'Você brincou com {bichos[selec].get_nome()} {turnos} vezes.')

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '5':

        if len(bichos) != 0:
            if selec == 'hoohaa':
                opcao = input('Deseja alterar fome(f), humor(h), saúde(s) ou idade(i)? ')
                value = input('Insira o novo valor: ')
                value = validador(value, 'i')
                if opcao.lower() == 'f':
                    for i in range(len(bichos)):
                        bichos[i].set_fome(value)
                    print(f'A fome de todos os bichos foi alterada para {value}')
                elif opcao.lower() == 'h':
                    for i in range(len(bichos)):
                        bichos[i].set_humor(value)
                    print(f'O humor de todos os bichos foi alterado para {value}')
                elif opcao.lower() == 's':
                    for i in range(len(bichos)):
                        bichos[i].set_saude(value)
                    print(f'A saude de todos os bichos foi alterada para {value}')
                elif opcao.lower() == 'i':
                    for i in range(len(bichos)):
                        bichos[i].set_idade(value)
                    print(f'A idade de todos os bichos foi alterada para {value}')
                else:
                    print('Opção inválida')

            else:
                opcao = input('Deseja alterar fome(f), humor(h), saúde(s) ou idade(i)? ')
                value = input('Insira o novo valor: ')
                value = validador(value, 'i')
                if opcao.lower() == 'f':
                    bichos[selec].set_fome(value)
                    print(f'A fome de {bichos[selec].get_nome()} foi alterada para {value}')
                elif opcao.lower() == 'h':
                    bichos[selec].set_humor(value)
                    print(f'O humor de {bichos[selec].get_nome()} foi alterado para {value}')
                elif opcao.lower() == 's':
                    bichos[selec].set_saude(value)
                    print(f'A saúde de {bichos[selec].get_nome()} foi alterada para {value}')
                elif opcao.lower() == 'i':
                    bichos[selec].set_idade(value)
                    print(f'A idade de {bichos[selec].get_nome()} foi alterada para {value}')
                else:
                    print('Opção inválida')

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '6':

        if len(bichos) != 0:
            if selec == 'hoohaa':
                for i in range(len(bichos)):
                    bichos[i].agradecimento()

            else:
                bichos[selec].agradecimento()

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '7':

        if len(bichos) != 0:
            if selec == 'hoohaa':
                for i in range(len(bichos)):
                    intel = bichos[i].get_porta()
                    print(f'Nome: {intel[0]} | Idade: {intel[1]} | Fome: {intel[2]}| Saúde: {intel[3]} '
                        f'| Humor: {intel[4]}')
            else:
                intel = bichos[selec].get_porta()
                print(f'Nome: {intel[0]} | Idade: {intel[1]} | Fome: {intel[2]}| Saúde: {intel[3]} | Humor: {intel[4]}')

        else:
            print('Primeiro você deve criar um bichinho!')

    elif acao == '0':
        break

    else:
        print('Ação inválida.')

print()
print('powered by ggOS')
