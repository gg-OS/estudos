from math import ceil


class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        self.perimetro = (2 * self.base) + (2 * self.altura)

    def valor_lados(self):
        print(f'Largura = {self.base} cm')
        print(f'Comprimento = {self.altura} cm')
        return

    def mudar_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura
        print('Valores alterados.')
        return

    def calcular_parimetro(self):
        print(f'Valor do perímetro = {self.perimetro} cm')
        return

    def calcular_area(self):
        print(f'Área do retângulo = {self.area} cm²')
        return

    def ladrilhos(self, vpiso, vrodape):
        total_rodape = self.perimetro / vrodape
        total_piso = self.area / (vpiso * vpiso)
        print(f'Quantidade de rodapés necessários: {ceil(total_rodape)}')
        print(f'Quantidade de pisos necessários: {ceil(total_piso)}')
        return


piso = None
rodape = None
print('Mini calculadora de piso')
largura = input('Insira o valor da largura da sala: ')
largura = float(largura)
comprimento = input('Insira o valor do comprimento da sala: ')
comprimento = float(comprimento)

sala = Retangulo(largura, comprimento)

print('Menu:\n'
      '1 - Visualizar medidas da sala\n'
      '2 - Alterar medidas da sala\n'
      '3 - Inserir medidas do piso e rodapé\n'
      '4 - Calcular área e perímetro da sala\n'
      '5 - Informar a quantidade de pisos e rodapés necessários\n'
      '0 - Encerrar aplicação')

while True:

    print()
    acao = input('Insira a ação desejada: ')

    if acao == '1':
        sala.valor_lados()

    elif acao == '2':
        largura = float(input('Insira o novo valor da largura: '))
        comprimento = float(input('Insira o novo valor do comprimento: '))
        sala.mudar_valor_lados(largura, comprimento)

    elif acao == '3':
        piso = float(input('Insira a largura do piso: '))
        rodape = float(input('Insira o tamanho do rodapé: '))
        print()
        print('Valores inseridos.')

    elif acao == '4':
        sala.calcular_parimetro()
        sala.calcular_area()

    elif acao == '5':
        if piso and rodape is not None:
            sala.ladrilhos(piso, rodape)
        else:
            print('Primeiro você deve informar os valores do piso e rodapé.')
    elif acao == '0':
        break

    else:
        print('Ação inválida')
        continue

print('Obrigado por utilizar o software')
print()
print('powered by ggOS')
