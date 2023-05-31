def inserir_valor():
    while True:
        valor = input('Insira o valor do lado do quadrado: ')
        try:
            valor = float(valor)
            break
        except ValueError:
            print('Valor inválido.')
            continue
    return valor


class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado
        return self.lado

    def valor_lado(self):
        return self.lado

    def area(self):
        area = self.lado * self.lado
        return area


print('Programa do quadrado')
q = Quadrado(inserir_valor())

while True:
    acao = input('Insira a ação desejada: \n'
                 '1 - Alterar o valor do lado\n'
                 '2 - Exibir o valor do lado\n'
                 '3 - Calcular área\n'
                 '4 - Encerrar programa\n')
    if acao == '1':
        q.mudar_lado(inserir_valor())
        print(f'O valor do lado foi alterado para {q.valor_lado()}')
    elif acao == '2':
        print(f'Lado do quadrado = {q.valor_lado()}')
    elif acao == '3':
        print(f'A área do quadrado é de {q.area()}')
    elif acao == '4':
        break
    else:
        print('Ação inválida.')

print()
print('powered by ggOS')
