
class Bola:

    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material

    def troca_cor(self, cor):
        if cor == self.cor:
            print(f'A cor {self.cor} já é a cor a bola.')
            return
        else:
            self.cor = cor
            print(f'Agora a bola é {self.cor}.')
            return

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}.')
        return


print('Bem vindo ao algoritmo da bola!')
cor = input('Escolha a cor da bola: ')
circ = input('Insira a circunferência da bola: ')
material = input('Insira o material que compõe a bola: ')
b = Bola(cor, circ, material)

while True:
    acao = input('O que deseja fazer?\n'
                 '1 - Mostrar cor da bola\n'
                 '2 - Trocar cor da bola\n'
                 '3 - Encerrar programa\n')
    if acao == '1':
        b.mostra_cor()
        print()
    elif acao == '2':
        cor = input('Insira a cor desejada: ')
        print()
        b.troca_cor(cor)
        print()
    elif acao == '3':
        break
    else:
        print('Ação inválida.\n')
        print()

print()
print('powered by ggOS')
