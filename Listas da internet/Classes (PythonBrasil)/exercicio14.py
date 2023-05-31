class Funcionario:

    def __init__(self, n, sal):
        self.nome = n
        self.salario = sal

    def get_info(self):
        return self.nome, self.salario

    def set_salario(self, sal):
        self.salario = salario
        print(f'O salário de {self.nome} foi alterado para {self.salario}')


funcionarios = []

print('Menu:\n'
      '1 - Inserir funcionário\n'
      '2 - Ver lista de funcionários\n'
      '3 - Alterar salário de um funcionário\n'
      '0 - Encerrar programa\n')

while True:

    acao = input('Insira a ação desejada: ')

    if acao == '1':
        nome = input('Insira o nome do funcionário: ')
        salario = input('Insira o salário do funcionário: ')
        funcionarios.append(Funcionario(nome, salario))

    elif acao == '2':
        for i in range(len(funcionarios)):
            print(f'{[i]} | {funcionarios[i].get_info()[0]} | R$ {funcionarios[i].get_info()[1]}')

    elif acao == '3':
        func = input('Insira o índice do funcionário: ')
        func = int(func)
        salario = input(f'{funcionarios[func].get_info()[0]} foi selecionado. Insira seu novo salário: ')
        funcionarios[func].set_salario(salario)

    elif acao == '0':
        break

    else:
        print('Ação inválida.')

print()
print('powered by ggOS')
