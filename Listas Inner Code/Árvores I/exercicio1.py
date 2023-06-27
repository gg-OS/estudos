from random import randint


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, itr, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if value < itr.value:
                if itr.left is None:
                    itr.left = Node(value)
                else:
                    self.insert(itr.left, value)
            else:
                if itr.right is None:
                    itr.right = Node(value)
                else:
                    self.insert(itr.right, value)


def count_nodes(itr, c):  # itr must be tree's root
    if itr is None:
        return c
    else:
        c += 1
        c = count_nodes(itr.left, c)
        c = count_nodes(itr.right, c)
        return c


binary_tree = Tree()

x = randint(5, 35)
for i in range(x):
    binary_tree.insert(binary_tree.root, randint(-10, 10))

print(x)
print(count_nodes(binary_tree.root, 0))
