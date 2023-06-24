class Node:

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            itr = self.head
            while itr.nxt:
                itr = itr.nxt
            itr.nxt = new_node
        return

    def show_list(self):
        itr = self.head
        linked_list = '['
        while itr:
            linked_list = linked_list + str(itr.data) + ' -> '
            itr = itr.nxt
        linked_list += 'None]'
        return linked_list

    def remove_duplicates(self):
        itr = self.head
        uniques = [itr.data]
        while itr.nxt is not None:
            if itr.nxt.data not in uniques:
                uniques.append(itr.nxt.data)
                itr = itr.nxt
            else:
                itr.nxt = itr.nxt.nxt
        return vector.show_list()


vector = LinkedList()

vector.insert(0)
vector.insert(1)
vector.insert(1)
vector.insert(5)
vector.insert(7)
vector.insert(10)
vector.insert(10)

print(f'Lista original: {vector.show_list()}\n')

print(f'Lista limpa: {vector.remove_duplicates()}\n')

print('powered by ggOS')
