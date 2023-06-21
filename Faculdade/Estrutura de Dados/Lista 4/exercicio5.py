from random import randint


class Node:

    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class Stack:

    def __init__(self):
        self.top = None

    def insert(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            mem = self.top
            self.top = new_node
            self.top.prev = mem
        return

    def print_stack(self):
        itr = self.top
        stack = ''
        for j in range(0, self.size()):
            stack = ' <- ' + str(itr.data) + stack
            itr = itr.prev
        stack = '[None' + stack
        stack += ']'
        return stack

    def pop(self):
        if self.top is None:
            print('A pilha está vazia')
            return
        else:
            show = self.top.data
            self.top = self.top.prev
        return show

    def size(self):
        s = 0
        itr = self.top
        if itr is None:
            print('A pilha está vazia.')
        else:
            while itr:
                s += 1
                itr = itr.prev
        return s


my_stack = Stack()
lista = []
for i in range(0, 5):
    num = randint(1, 20)
    lista.append(num)
    my_stack.insert(num)
print(f'A lista ficou assim: {lista}')

print('\nO visual da pilha ficou da seguinte forma:')
print(my_stack.print_stack())

print('\nNa ordem inversa, fica assim:')
for i in range(my_stack.size()):
    print(my_stack.pop())

print('\npowered by ggOS')
