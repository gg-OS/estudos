from random import randint


class Node:

    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class Stack:

    def __init__(self):
        self.top = None

    def insert_elem(self, elem):
        new_node = Node(elem)
        if self.top is None:
            self.top = new_node
        else:
            mem = self.top
            self.top = new_node
            self.top.prev = mem
        return

    def pop_elem(self):
        if self.top is None:
            print('Pilha vazia.')
            return
        else:
            mem = self.top.data
            self.top = self.top.prev
        return mem

    def show_stack(self):
        itr = self.top
        stack = ''
        if self.top is None:
            stack = 'Empty stack'
        else:
            while itr:
                stack += ' <- ' + str(itr.data)
                itr = itr.prev
        stack = '[None' + stack
        stack = stack + ']'
        return str(stack)


lista = []
my_stack = Stack()

for i in range(15):
    lista.append(randint(0, 50))

print(f'A lista ficou: {lista}\n')

for elemento in lista:
    if elemento % 2 == 0:
        my_stack.insert_elem(elemento)
    else:
        my_stack.pop_elem()

print(f'Pilha: {my_stack.show_stack()}\n')

print('powered by ggOS')
