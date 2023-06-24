from random import randint
from time import sleep


class Node:

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class CircularList:

    def __init__(self):
        self.head = None

    def inserir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.nxt = self.head
        else:
            itr = self.head
            if itr.nxt == self.head:
                self.head.nxt = new_node
                new_node.nxt = self.head
            else:
                while itr.nxt != self.head:
                    itr = itr.nxt
                new_node.nxt = self.head
                itr.nxt = new_node
        return

    def exibir(self):
        itr = self.head
        if self.head is None:
            return None
        else:
            circled_list = '[-> '
            while True:
                if itr.nxt == self.head:
                    break
                circled_list = circled_list + str(itr.data) + ' -> '
                itr = itr.nxt
            circled_list += ']'
            return circled_list


class LinkedList:

    def __init__(self):
        self.head = None

    def inserir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            itr = self.head
            while itr.nxt:
                itr = itr.nxt
            itr.nxt = new_node
        return

    def exibir(self):
        itr = self.head
        linked_list = '['
        while itr:
            linked_list = linked_list + str(itr.data) + ' -> '
            itr = itr.nxt
        linked_list += 'None]'
        return linked_list


def verificador(lista):
    itr = lista.head
    resultado = ''
    while True:
        if itr.nxt is None:
            resultado = 'Não é uma lista circular'
            return resultado

        elif itr.nxt == lista.head:
            resultado = 'Lista circular'
            return resultado

        else:
            itr = itr.nxt


print('Welcome to challenge #3\n')

print('Deploying in 3 seconds...\n')
sleep(3)


list_1 = LinkedList()
list_2 = CircularList()

for i in range(0, 10):
    list_1.inserir(randint(10, 40))
    list_2.inserir(randint(30, 90))

print(f'Lista 1: {list_1.exibir()}')
print(f'Lista 2: {list_2.exibir()}')

print('\nRunning tests...\n')
sleep(2)

print(f'Lista 1: {verificador(list_1)}')
print(f'Lista 2: {verificador(list_2)}')

print('\npowered by ggOS')
