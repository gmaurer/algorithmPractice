from assets import node

class LinkedList:
    def __init__(self):
        self.head = None

    def push_to_front(self,new_data):
        new_node = node.LLNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node, new_data):
        if prev_node is None:
            print("Previous node is None")
            return

        new_node = node.LLNode(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = node.LLNode(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse_list(self):
        if self.head is None:
            print("Empty LL")
            return

        if self.head.next is None:
            print(self.head.data, "1 Node")
            return
        curr_prev = self.head
        curr = curr_prev.next
        curr_next = curr.next
        curr_prev.next = None
        
        while(curr_next):
            curr.next = curr_prev
            curr_prev = curr
            curr = curr_next
            curr_next = curr.next
        curr.next = curr_prev
        self.head = curr
