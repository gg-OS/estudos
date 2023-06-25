from random import randint


class Node:

    def __init__(self, data, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_elem(self, element):
        new_node = Node(element)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.head == self.tail:
                self.tail = new_node
                self.tail.nxt = self.head
            else:
                mem = self.tail
                self.tail = new_node
                self.tail.nxt = mem
        return

    def pop_elem(self):
        if self.head is None:
            print('A fila está vazia.')
            return
        else:
            itr = self.tail
            while itr.nxt != self.head:
                itr = itr.nxt
            mem = self.head
            self.head = itr
        return mem

    def print_queue(self):
        itr = self.tail
        queue = ''
        if self.head is None:
            print('A fila está vazia.')
        else:
            while itr:
                queue = str(itr.data) + ' <- ' + queue
                itr = itr.nxt
            queue = queue[:-4] + ']'
            queue = '[' + queue
        return queue

    def find_index(self, index):
        itr = self.tail
        for j in range(index, 0, -1):
            itr = itr.nxt
        return itr


def inversor(fila):
    vetor_2 = []
    itr = fila.tail
    while itr:
        vetor_2.append(itr.data)
        itr = itr.nxt
    return vetor_2


my_queue = Queue()
vetor = []

for i in range(5):
    vetor.append(randint(0, 20))

print(f'Vetor = {vetor}\n')

print('Inserindo elementos...\n')

for elem in vetor:
    my_queue.insert_elem(elem)

print(f'Fila: {my_queue.print_queue()}\n')
novo_vetor = inversor(my_queue)

nova_fila = Queue()
for k in novo_vetor:
    nova_fila.insert_elem(k)

print(f'Fila invertida = {nova_fila.print_queue()}\n')

print('powered by ggOS')
