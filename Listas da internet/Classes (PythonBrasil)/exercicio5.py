class ContaCorrente:

    def __init__(self, nc, nomec):
        self.numero_conta = nc
        self.nome_conta = nomec
        self.saldo = 0

    def alterar_nome(self, nomec):
        self.nome_conta = nomec
        print(f'Nome da conta alterado para {self.nome_conta}')
        return

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito realizado. Seu saldo agora é de R${self.saldo}')

    def saque(self, valor):
        if self.saldo == 0:
            print('Você não possui saldo para realizar um saque.')
        else:
            if valor > self.saldo:
                print('Você não possui saldo suficiente.')
            else:
                self.saldo -= valor
                print(f'Saque realizado. Seu saldo agora é de R${self.saldo}')
        return


print('ggOS bank')
numero_conta = input('Insira o número da conta: ')
nome_conta = input('Insira o nome da conta: ')
conta = ContaCorrente(numero_conta, nome_conta)

print('Menu:\n'
      '1 - Alterar nome da conta\n'
      '2 - Depositar dinheiro\n'
      '3 - Sacar dinheiro\n'
      '0 - Encerrar\n')

while True:

    acao = input('Insira a ação desejada: ')

    if acao == '1':
        nome_conta = input('Insira o novo nome da conta: ')
        conta.alterar_nome(nome_conta)

    elif acao == '2':
        quantia = input('Insira a quantia que deseja depositar: ')
        quantia = float(quantia)
        conta.deposito(quantia)

    elif acao == '3':
        quantia = input('Insira a quantia que deseja sacar: ')
        quantia = float(quantia)
        conta.saque(quantia)

    elif acao == '0':
        print('Encerrando aplicação')
        break

    else:
        print('Ação inválida.')

print()
print('powered by ggOS')
