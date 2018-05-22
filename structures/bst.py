from assets import node

def binary_search_tree(numbers):
    root = None
    for x in numbers:
        root = create_tree(root, int(x))
    return root


def create_tree(node1,number):
    if not node1:
        return node.Node(number)
    elif number > node1.value:
        node1.right = create_tree(node1.right, number)
    elif number < node1.value:
        node1.left = create_tree(node1.left, number)
    return node1
#def insert_node():
