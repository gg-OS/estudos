"""
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso
"""


class Carro:

    def __init__(self, combustivel, consumo):
        self.combustivel = combustivel
        self.consumo = consumo
        self.rodagem = 0

    def andar(self, value):
        self.combustivel -= (value / self.consumo)
        if self.combustivel >= 0:
            self.rodagem += value
            return value, self.rodagem, self.combustivel
        else:
            self.combustivel += (value / self.consumo)
            print('Você não possui gasolina suficiente')

    def set_gasolina(self, value_2):
        self.combustivel += value_2
        print(f'Você abasteceu {value_2} litros de combustível.')

    def get_gasolina(self):
        return self.combustivel

while True:
    consumo = input('Insira o valor do consumo do carro em km/litro: ')
    combustivel = input('Insira a quantidade de combustível presente no carro: ')
    try:
        consumo = float(consumo)
        combustivel = float(combustivel)
        break
    except ValueError:
        print('Dados inválidos.')


hotwheels = Carro(combustivel, consumo)

print('Menu:\n'
      '1 - Andar\n'
      '2 - Abastecer\n'
      '3 - Verificar combustível\n'
      '0 - Encerrar programa\n')


while True:

    acao = input('Escolha uma ação: ')

    if acao == '1':

        valor = input('Insira o quanto deseja andar em km:  ')
        valor = float(valor)
        resultado = hotwheels.andar(valor)

        print(f'Você andou {resultado[0]}km , restando {resultado[2]}L de combustível. Total rodado = {resultado[1]}km.')

    elif acao == '2':

        valor = input('Insira quantos litros de combustível deseja abastecer: ')
        valor = float(valor)
        hotwheels.set_gasolina(valor)
        print()

    elif acao == '3':

        resultado = hotwheels.get_gasolina()
        print(f'Você possui {resultado} de gasolina.')

    elif acao == '0':
        break

    else:
        while True:
         print('Ação inválida')
