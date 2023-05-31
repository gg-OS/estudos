class Televisao:

    def __init__(self):
        self.canal = 1
        self.volume = 5

    def alterar_volume(self, vol):
        if vol is True:
            if self.volume != 10:
                self.volume += 1
        else:
            if self.volume != 1:
                self.volume -= 1
        print(f'Volume: {self.volume}')
        return

    def alterar_canal(self, ch):
        if ch is True:
            if self.canal != 10:
                self.canal += 1
        else:
            if self.canal != 1:
                self.canal -= 1
        print(f'Canal: {self.canal}')
        return

    def informacoes(self):
        print(f'Canal atual: {self.canal}')
        print(f'Volume atual: {self.volume}')
        return


print('TV DE TUBO ggOS')

tv = Televisao()
print()
print('Controle:\n'
      '1 - Aumentar canal\n'
      '2 - Diminuir canal\n'
      '3 - Aumentar volume\n'
      '4 - Diminuir volume\n'
      '5 - Informar canal e volume\n'
      '0 - Desligar\n')

while True:
    acao = input('Aperte um botão: ')

    if acao == '1':
        c = True
        tv.alterar_canal(c)

    elif acao == '2':
        c = False
        tv.alterar_canal(c)

    elif acao == '3':
        v = True
        tv.alterar_volume(v)

    elif acao == '4':
        v = False
        tv.alterar_volume(v)
    elif acao == '5':
        tv.informacoes()

    elif acao == '0':
        print('Desligando a tv...')
        break

    else:
        print('Ação inválida')
