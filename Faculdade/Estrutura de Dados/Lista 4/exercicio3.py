class Node:

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:

    def __init__(self):
        self.head = None

    def inserir(self, elem):
        novo_node = Node(elem)
        if self.head is None:
            self.head = novo_node
        else:
            itr = self.head
            while itr.nxt:
                itr = itr.nxt
            itr.nxt = novo_node

        return

    def remover(self, ind):
        itr = self.head
        for k in range(0, ind - 1):
            itr = itr.nxt
        itr.nxt = itr.nxt.nxt
        return

    def buscar(self, ind):
        itr = self.head
        for j in range(0, ind):
            itr = itr.nxt

        return itr.data

    def exibir(self):
        itr = self.head
        lista_exibir = '['
        while itr:
            lista_exibir = lista_exibir + str(itr.data) + ' -> '
            itr = itr.nxt
        lista_exibir += 'None]'

        return lista_exibir

    def tamanho(self):
        c = 0
        itr = self.head
        while itr:
            itr = itr.nxt
            c += 1

        return c


lista_encadeada = LinkedList()

for i in range(1, 20, 2):
    lista_encadeada.inserir(i)

print('Menu de opções: \n'
      '1- Visualizar lista atual\n'
      '2 - Buscar índice específico\n'
      '3 - Remover índice específico\n'
      '4 - Inserir novo elemento\n'
      '0 - Encerrar programa\n')

while True:
    indice = input('Insira a opção desejada: ')

    try:
        indice = int(indice)
    except ValueError:
        print('Entrada inválida.\n')

    if indice == 1:
        print(f'Lista atual: {lista_encadeada.exibir()}\n')

    elif indice == 2:
        n = input('Insira o índice que deseja buscar dentro da lista: ')
        try:
            n = int(n)
            if indice >= lista_encadeada.tamanho():
                print('Indice inexistente.\n')
            else:
                print(f'lista[{n}] = {lista_encadeada.buscar(n)}')
        except ValueError:
            print('Indice inválido.\n')

    elif indice == 3:
        n = input('Insira o índice que deseja remover dentro da lista: ')
        try:
            n = int(n)
            if indice >= lista_encadeada.tamanho():
                print('Indice inexistente.\n')
            else:
                valor = lista_encadeada.buscar(n)
                lista_encadeada.remover(n)
                print(f'O valor {valor} no índice lista[{n}] foi removido.\n')
        except ValueError:
            print('Indice inválido.\n')

    elif indice == 4:
        elemento = input('Insira o elemento que deseja inserir: ')
        try:
            elemento = int(elemento)
            lista_encadeada.inserir(elemento)
        except ValueError:
            print('Elemento inválido, por favor insira apenas números inteiros.')

    elif indice == 0:
        print('\nEncerrando o programa...\n')
        break

    else:
        print('Opção não existente.\n')

print('powered by ggOS')
