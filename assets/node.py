import random

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

    def add_node(self,parent, value):
        if parent.left is None:
            parent.left = Node(value)
        elif parent.right is None:
            parent.right = Node(value)
        else:
            print("Left and Right Full")

    def add_one_node(self, value):
        self.value = value

    def create_random_node(self, height):
        #height balanced tree
        if height > 1:
            self.left = Node(random.randint(1,99))
            self.left.create_random_node(height - 1)

            self.right = Node(random.randint(1,99))
            self.right.create_random_node(height - 1)


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLLNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
