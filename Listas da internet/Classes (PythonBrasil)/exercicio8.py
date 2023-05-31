class Macaco:

    def __init__(self, name):
        self.nome = name
        self.bucho = []

    def ver_nome(self):
        return self.nome

    def comer(self, a):
        self.bucho.append(a)
        print(f'{self.nome} foi alimentado com {a}')

    def ver_bucho(self):
        if len(self.bucho) != 0:
            print(f'O bucho de {self.nome} contém {self.bucho}')
        else:
            print(f'O bucho de {self.nome} está vazio.')

    def digerir(self):
        print(f'{self.nome} agora está com o buchinho vazio.')
        self.bucho = []

    def waaaa(self):
        print(f'{self.nome}: "WAAAAAAAAAAAAAAA"')


macacos = {}
c = 1
nomes = []
print('Menu de ações:\n'
      '1 - Criar um macaco\n'
      '2 - Selecionar um macaco\n'
      '3 - Alimentar macaco selecionado\n'
      '4 - Ver o bucho do macaco selecionado\n'
      '5 - Digerir o alimento\n'
      '6 - WAAAAAAAAA (comunicar-se com os macacos em macaquês)\n'
      '0 - Encerrar programa do macaco\n')

selec = False

while True:
    acao = input('Insira a ação desejada: ')
    if acao == '1':

        nome = input('Insira o nome do macaco que deseja criar: ')
        macacos.update({c: nome.title()})
        nomes.append(nome.title())
        macacos[c] = Macaco(nome.title())
        c += 1

    elif acao == '2':

        if len(macacos) != 0:
            for item in macacos.keys():
                print(f'{item} | {macacos[item].ver_nome()}')
            selec = input('Selecione o macaco pelo índice: ')
            while True:
                try:
                    selec = int(selec)
                    break
                except ValueError or IndexError:
                    print('Índice inválido.')
                    continue
            print(f'{macacos[selec].ver_nome()} é o macaco selecionado.')
        else:
            print('Não há macacos disponíveis para seleção.')

    elif acao == '3':

        if selec is not False:
            alimento = input(f'O que deseja dar para {macacos[selec].ver_nome()} comer? ')
            if alimento in nomes:
                print('Canibalismo é proibido na macacolândia')
            else:
                macacos[selec].comer(alimento.title())
        else:
            print('Primeiro você deve criar um macaco.')

    elif acao == '4':

        if selec is not False:
            macacos[selec].ver_bucho()
        else:
            print('Primeiro você deve criar um macaco.')

    elif acao == '5':

        if selec is not False:
            macacos[selec].digerir()
        else:
            print('Primeiro você deve criar um macaco.')

    elif acao == '6':
        macacos[selec].waaaa()

    elif acao == '0':
        break

    else:
        print('Ação inválida.')

print('FIM DO PROGRAMA DA MACACOLÂNDIA\n')
print('powered by ggOS')
