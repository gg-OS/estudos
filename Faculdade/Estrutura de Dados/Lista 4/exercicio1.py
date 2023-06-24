class Node:

    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.proximo = proximo


class LinkedList:

    def __init__(self):
        self.head = None

    def exibir(self):
        if self.head is None:
            print('Lista encadeada está vazia')
            return

        iterador = self.head
        le = ''
        while iterador:
            le += str(iterador.dado) + ' -> '
            iterador = iterador.next

        print(le)

    def adicionar_no_inicio(self, dado):
        novo_node = Node(dado, self.head)
        if self.head is None:
            self.head = novo_node
        else:
            novo_node.next = self.head
            self.head = novo_node

    def buscar_valor(self, valor):
        iterador = self.head
        informacao = None
        while iterador.next:
            if valor == iterador.dado:
                informacao = iterador
                return print(f"O valor está no nó: {informacao}")
            iterador = iterador.next
        if informacao is None:
            return print("O valor não foi encontrado na lista encadeada")

    def remover_valor(self, valor):
        assert self.head, "Impossível remover valor de lista vazia"
        if self.head.dado == valor:
            self.head = self.head.next
        else:
            anterior = None
            iterador = self.head
            while iterador is not None and iterador.dado != valor:
                anterior = iterador
                iterador = iterador.next
            if iterador:
                anterior.proximo = iterador.next
            else:
                anterior.proximo = None


lista_encadeada = LinkedList()
opcao = ''

print("Insira a opção:\n"
      "1 - Inserir valor\n"
      "2 - Remover valor\n"
      "3 - Ver lista\n"
      "0 - Encerrar programa\n")

while opcao != '0':

    opcao = input("Insira a opção desejada: ")

    if opcao == '1':
        value = input("Insira o valor desejado: ")
        try:
            value = int(value)
        except ValueError:
            value = str(value)
        lista_encadeada.adicionar_no_inicio(value)
        print("\nValor inserido.\n")

    elif opcao == '2':
        value = input("Insira o valor que deseja remover")
        lista_encadeada.remover_valor(value)
        print("\nValor removido.\n")

    elif opcao == '3':
        print(f'Lista: {lista_encadeada.exibir()}')

    elif opcao == '0':
        break

    else:
        print("Opção inválida")
