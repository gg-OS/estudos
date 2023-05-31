class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_info(self):
        return self.nome, self.salario


funcionarios = []

print('Menu:\n'
      '1 - Inserir funcionário\n'
      '2 - Ver lista de funcionários\n'
      '0 - Encerrar programa\n')

while True:

    acao = input('Insira a ação desejada: ')

    if acao == '1':
        nome = input('Insira o nome do funcionário: ')
        salario = input('Insira o salário do funcionário: ')
        funcionarios.append(Funcionario(nome, salario))

    elif acao == '2':
        for i in range(len(funcionarios)):
            print(f'{funcionarios[i].get_info()[0]} | R$ {funcionarios[i].get_info()[1]:.2f}')

    elif acao == '0':
        break

    else:
        print('Ação inválida.')

print()
print('powered by ggOS')
