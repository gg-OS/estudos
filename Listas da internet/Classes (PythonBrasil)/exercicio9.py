"""
a. Possua uma classe chamada Ponto, com os atributos x e y. (ok)
b. Possua uma classe chamada Retangulo, com os atributos largura e altura. (ok)
c. Possua uma função para imprimir os valores da classe Ponto. (ok)
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um
objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os
valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""
# y3 = y2, y1 = y4, x1 = x2, x3 = x4


class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_points(self):
        return self.x, self.y


class Retangulo:

    def __init__(self, l, h, xi, xf, yi, yf, pts):
        self.largura = l
        self.altura = h
        self.centro = ((xf + xi) / 2, (yf + yi) / 2)
        self.pontos = pts

    def get_center(self):
        return self.centro

    def get_info(self):
        return self.largura, self.altura

    def get_pts(self):
        return self.pontos


def criar_retangulo():
    pontos = []
    for i in range(4):
        while True:
            coord_x = input(f'Insira a coordenada x do {i + 1}º ponto: ')
            coord_y = input(f'Insira a coordenada y do {i + 1}º ponto: ')
            try:
                coord_x = float(coord_x)
                coord_y = float(coord_y)
                break
            except ValueError:
                print('Insira apenas valores numéricos.')
        pontos.append((coord_x, coord_y))
    return pontos


selec = 0
retangulos = []

print('Programa de criação de retângulos ggOS\n')

print('Menu de ações:\n'
      '1 - Criar retângulo\n'
      '2 - Selecionar retângulo\n'
      '3 - Ver pontos do retângulo\n'
      '4 - Imprimir centro do retângulo\n'
      '0 - Encerrar programa\n')

while True:
    acao = input('Insira a ação desejada: ')

    if acao == '1':
        pontos = criar_retangulo()
        print(pontos)
        if pontos[0][0] == pontos[1][0] and pontos[2][0] == pontos[3][0] and pontos[0][1] == pontos[3][1] and pontos[1][1] == pontos[2][1]:
            largura = pontos[3][1] - pontos[0][1]
            altura = pontos[3][0] - pontos[2][0]
            x_inicial = pontos[3][0]
            x_final = pontos[0][0]
            y_inicial = pontos[3][1]
            y_final = pontos[2][1]
            for k in range(len(pontos)):
                pontos[k] = Ponto(pontos[k][0], pontos[k][1])
            retangulos.append(Retangulo(largura, altura, x_inicial, x_final, y_inicial, y_final, pontos))
            print(retangulos)
        else:
            print('Retângulo inválido')

    elif acao == '2':

        if len(retangulos) != 0:
            for z in range(len(retangulos)):
                print(f'{z + 1} | Retângulo {z + 1}')
            selec = input('Selecione o retângulo: ')
            while True:
                try:
                    selec = int(selec) - 1
                    break
                except ValueError or IndexError:
                    print('Índice inválido.')
                    continue
            print(f'Retângulo {selec + 1} foi selecionado.')
        else:
            print('Primeiro você deve criar um retângulo.')

    elif acao == '3':

        print('LAMENTAVELMENTE NÃO TIVE CAPACIDADE DE RESOLVER ISSO A TEMPO HÁBIL')

    elif acao == '4':

        if len(retangulos) != 0:
            print(f'{retangulos[selec].get_center()} é o centro do retângulo.')

    elif acao == '0':
        break

    else:
        print('Insira uma ação válida.\n')

print()
print('Você encerrou o programa.\n')
print('powered by ggOS')
