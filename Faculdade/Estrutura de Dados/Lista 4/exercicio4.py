from random import randint


class Node:

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class Stack:

    def __init__(self, top=None):
        self.top = top

    def insert(self, data):

        if self.top is None:
            self.top = Node(data)

        else:
            itr = self.top
            while itr.nxt is not None:
                itr = itr.nxt
            itr.nxt = Node(data)

        return

    def show(self):
        itr = self.top
        stack = '['

        if itr is None:
            print('A Pilha está vazia.')
            return

        else:
            while itr:
                stack = stack + str(itr.data) + ' -> '
                itr = itr.nxt

        stack = stack + 'None]'
        return stack

    def bigger(self):
        itr = self.top
        bigger = itr.data

        if itr is None:
            print('A pilha está vazia.')
            return

        else:
            while itr:
                if itr.data > bigger:
                    bigger = itr.data
                itr = itr.nxt
        return bigger


my_stack = Stack()
for i in range(0, 10):
    my_stack.insert(randint(1, 100))

print(f'A pilha ficou: {my_stack.show()}')
print(f'O maior elemento da pilha é: {my_stack.bigger()}')

print('\npowered by ggOS')
