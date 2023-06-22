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


positive = Stack()
negative = Stack()

numeros = []

for i in range(20):
    numeros.append(randint(-50, 50))

print(f'Vetor => {numeros}\n')

for elemento in numeros:
    if elemento > 0:
        positive.insert_elem(elemento)
    elif elemento < 0:
        negative.insert_elem(elemento)
    else:
        positive.pop_elem()
        negative.pop_elem()

print(f'Positivos: {positive.show_stack()}')
print(f'Negativos: {negative.show_stack()}\n')

print('powered by ggOS')
