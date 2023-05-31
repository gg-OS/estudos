class BombaDeCombustivel:

    def __init__(self, tipo, valor, qtd):
        self.tipo = tipo
        self.valor = valor
        self.qtd = qtd

    def get_tipo(self):
        return self.tipo

    def get_value(self):
        return self.valor

    def get_amount(self):
        return self.qtd

    def abastecerPorValor(self, val):
        volume = val / self.valor
        self.qtd -= volume
        return volume

    def abastecerPorLitro(self, vol):
        custo = vol * self.valor
        self.qtd -= vol
        return custo

    def set_value(self, valor):
        self.valor = valor

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_amount(self, qtd):
        self.qtd = qtd


bomba = {}
c = 1

print('Menu de ações: \n'
      '1 - Cadastrar combustível\n'
      '2 - Abastecer\n'
      '3 - Dados da bomba\n'
      '4 - Alterar dados da bomba\n'
      '0 - Encerrar\n')

while True:
    acao = input('Insira a ação desejada: ')

    if acao == '1':
        tipo = input('Qual tipo de combustível deseja cadastrar? ')
        while True:
            vol = input(f'Quanto em litros de {tipo} será inserido? ')
            preco = input(f'Qual o valor por litro de {tipo}? ')
            try:
                vol = float(vol)
                preco = float(preco)
                break
            except ValueError:
                print('Dados inválidos acerca do combustível')
        bomba.update({c: BombaDeCombustivel(tipo, preco, vol)})
        c += 1

    elif acao == '2':
        if len(bomba) != 0:
            for i in bomba.keys():
                print(f'{i} | {bomba[i].get_tipo()}')
            selec = input('Selecione um combustível: ')
            selec = int(selec)
            print(f'{bomba[selec].get_tipo()} foi selecionado.')
            acao_2 = input('Deseja abastecer por volume (1) ou valor (2)? ')
            if acao_2 == '1':
                selec_2 = input('Insira a quantidade de combustível: ')
                selec_2 = float(selec_2)
                print(f'Você abasteceu {selec_2}L de {bomba[selec].get_tipo()} '
                      f'a um custo de R$ {bomba[selec].abastecerPorLitro(selec_2)}')
            elif acao_2 == '2':
                selec_2 = input('Insira o valor que deseja pagar: ')
                selec_2 = float(selec_2)
                print(f'Você abasteceu {selec_2}L de {bomba[selec].get_tipo()} '
                      f'a um custo de R$ {bomba[selec].abastecerPorValor(selec_2)}')
            else:
                print('Ação inválida.\n')
                break
        else:
            print('Primeiro você deve cadastrar um combustível na bomba')

    elif acao == '3':

        if len(bomba) != 0:
            for i in bomba.keys():
                print(f'{i} | {bomba[i].get_tipo()} | R${bomba[i].get_value()} | {bomba[i].get_amount()} L')
        else:
            print('Primeiro você deve cadastrar um combustível na bomba')

    elif acao == '4':

        if len(bomba) != 0:
            for i in bomba.keys():
                print(f'{i} | {bomba[i].get_tipo()}')
            selec = input('Selecione o combustível a ser alterado: ')
            selec = int(selec)
            print(f'{bomba[selec].get_tipo()} foi selecionado.')
            selec_2 = input('Deseja alterar o valor(v) ou a quantidade(q)?')

            if selec_2 == 'v':
                alterar = input('Insira o novo valor: ')
                alterar = float(alterar)
                bomba[selec].set_value(alterar)
            else:
                alterar = input('Insira a nova quantidade: ')
                alterar = float(alterar)
                bomba[selec].set_amount(alterar)

        else:
            print('Primeiro você deve cadastrar um combustível na bomba')

    elif acao == '0':
        break

    else:
        print('Ação inválida.\n')

print()
