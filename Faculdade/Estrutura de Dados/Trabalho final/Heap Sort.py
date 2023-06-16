# Classe para representar o produto
class Produto:

    def __init__(self, nome, valor, next=None):
        self.nome = nome
        self.valor = valor
        self.next = next


# Lista encadeada para inserir os produtos
class ListaDeProdutos:

    def __init__(self):
        self.head = None

    # Método de inserção de produtos na lista
    def inserir(self, nome, valor):
        new_product = Produto(nome, valor)
        if self.head is None:
            self.head = new_product
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_product

    # Método para exibir produtos listados
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

    # Método para retornar tamanho da lista encadeada
    def tamanho(self):
        itr = self.head
        c = 0
        while itr:
            itr = itr.next
            c += 1
        return c

    # Método para retornar um produto de determinado índice
    def retornar_valor_indice(self, indice):
        itr = self.head
        if indice - 1 > self.tamanho():
            print('Índice inválido')
            return
        for i in range(0, indice):
            itr = itr.next
        return itr.valor


# Classe da árvore
class Node:

    def __init__(self, produto, esquerda=None, direita=None):
        self.produto = produto
        self.esquerda = esquerda
        self.direita = direita

    # Método para inserir produto na árvore
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


def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.produto),

    # Visita filho da direita.
    em_ordem(raiz.direita)


# Criação do objeto de lista encadeada com os produtos
lista_de_produtos = ListaDeProdutos()

# Usuário faz a inserção de produtos na lista
lista_de_produtos.inserir('MacBook Pro', 1999)
lista_de_produtos.inserir('Apple Vision Pro', 3499)
lista_de_produtos.inserir('Apple Watch', 399)
lista_de_produtos.inserir('iMac', 1699)
lista_de_produtos.inserir('iPhone', 999)

# Exibe a lista de produtos de forma não ordenada
print(lista_de_produtos.exibir())

# Inserindo elementos da lista na árvore
raiz = Node(lista_de_produtos.retornar_valor_indice(0))

for i in range(1, lista_de_produtos.tamanho()):
    elemento = lista_de_produtos.retornar_valor_indice(i)
    raiz.inserir(elemento)

em_ordem(raiz)


