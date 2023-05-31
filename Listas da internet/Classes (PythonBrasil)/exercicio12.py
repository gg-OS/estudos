class ContaInvestimento():

    def __init__(self, m, j):
        self.montante = m
        self.juros = j

    def set_tempo(self, tempo):
        self.montante = self.montante * ((self.juros) ** tempo)

    def get_montante(self):
        return self.montante


contas = {}
c = 1

print('Menu de ações: \n'
      '1 - Criar conta\n'
      '2 - Ver contas\n'
      '3 - Passar tempo\n'
      '0 - Encerrar programa\n')

while True:

    acao = input('Insira a ação selecionada: ')

    if acao == '1':
        contas.update({c: ContaInvestimento(1000, 1.0107)})
        c += 1
        print('Conta criada')

    elif acao == '2':
        for i in contas.keys():
            print(f'{i} | R$ {contas[i].get_montante():.2f}')

    elif acao == '3':
        t = input('Quantos meses deseja passar? ')
        t = int(t)
        for i in contas.keys():
            contas[i].set_tempo(t)

    elif acao == '0':
        break

    else:
        print('Insira uma ação válida.')

print()
print('powered by ggOS')
