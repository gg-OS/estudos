class Produto:

    def __init__(self, nome, valor, next=None):
        self.nome = nome
        self.valor = valor
        self.next = next


class ListaDeProdutos:

    def __init__(self):
        self.head = None

    def inserir(self, nome, valor):
        new_product = Produto(nome, valor)
        if self.head is None:
            self.head = new_product
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_product

    def exibir(self):
        if self.head is None:
            print('Lista de produtos vazia')
            return
        itr = self.head
        lista = ''
        while itr:
            lista += '(' + str(itr.nome) + ': ' + str(itr.valor) + ')' + ', '
            itr = itr.next
        return lista

"""
    def retornar_indice(self, indice):
        itr = self.head
        for i in range(0, indice):
            try:
                itr = itr.next
            except:

        return itr

    def tamanho(self):
        pass
"""

class Node:

    def __init__(self, produto, esquerda=None, direita=None):
        self.produto = produto
        self.esquerda = esquerda
        self.direita = direita

    def inserir(self, produto):
        if self.produto:
            if produto < self.produto:
                if self.esquerda is None:
                    self.esquerda = Node(produto)
                else:
                    self.esquerda.inserir(produto)
            elif produto > self.produto:
                if self.direita is None:
                    self.direita = Node(produto)
                else:
                    self.direita.inserir(produto)
            else:
                self.produto = produto

# Função de construir a árvore
    def construcao(self):
        pass

# Função de extrair elementos da árvore para ordenar o heap
    def extracao(self):
        pass


lista_de_produtos = ListaDeProdutos()
lista_de_produtos.inserir('MacBook Pro', 1999)
lista_de_produtos.inserir('Apple Vision Pro', 3499)
lista_de_produtos.inserir('Apple Watch', 399)
lista_de_produtos.inserir('iMac', 1699)
lista_de_produtos.inserir('iPhone', 999)

# Exibe a lista de produtos crua
print(lista_de_produtos.exibir())

# Inserindo elementos da lista na árvore
for i in range(0, 5):
    pass
