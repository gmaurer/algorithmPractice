from assets import node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_front(self, new_data):
        new_node = node.DoublyLLNode(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node = self.head.prev
        new_node.next = self.head
        self.head = new_node

    def append_rear(self, new_data):
        new_node = node.DoublyLLNode(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
