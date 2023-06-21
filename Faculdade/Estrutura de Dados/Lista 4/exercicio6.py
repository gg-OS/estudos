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

    def busca(self, index):
        itr = self.top
        for y in range(index):
            itr = itr.prev
        return itr.data


def verificador(s1, s2):
    c = 0
    for k in range(0, s1.size()):
        if s1.busca(k) == s2.busca(k):
            c += 1
    return c


def f(x): return ((1/fatores) ** x) * 100


stack1 = Stack()
stack2 = Stack()
tamanho = int(input('Insira o tamanho das pilhas: '))
fatores = 3

for i in range(0, tamanho):
    stack1.insert(randint(1, fatores))
    stack2.insert(randint(1, fatores))

print(f'Pilha 1: {stack1.print_stack()}')
print(f'Pilha 2: {stack2.print_stack()}')

print()

if verificador(stack1, stack2) == stack1.size():
    print()
    print('As pilhas são iguais.')
else:
    print('As pilhas são diferentes.')

print()
print('Bônus no código!!\n')
print(f'Probabilidade das pilhas serem iguais = {f(tamanho):.2f}%\n')

print('\npowered by ggOS')
