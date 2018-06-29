class tree_node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1
#create pointer class to see root node and allow the shift to happen there
#for readability.  Similar to Ians github avl C tree
class avl_tree(object):
    def insert(self, root, key):
        if not root:
            return(tree_node(key))
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.val:
            return(self.right_rotate(root))

        if balance < -1 and key > root.right.val:
            return(self.left_rotate(root))

        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return(self.right_rotate(root))

        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return(self.left_rotate(root))

        return(root)

    def left_rotate(self,node):
        right_node = node.right
        lower_left_node = right_node.left

        right_node.left = node
        node.right = lower_left_node

        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        right_node.height = 1 + max(self.get_height(right_node.left),self.get_height(right_node.right))

        return(right_node)

    def right_rotate(self,node):
        left_node = node.left
        lower_right_node = left_node.right

        left_node.right = node
        node.left = lower_right_node

        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        left_node.height = 1 + max(self.get_height(left_node.left),self.get_height(left_node.right))

        return(left_node)

    def get_balance(self, root):
        if not root:
            return 0
        return(self.get_height(root.left) - self.get_height(root.right))

    def get_height(self, root):
        if not root:
            return 0
        return(root.height)

    def preorder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preorder(root.left)
        self.preorder(root.right)

myTree = avl_tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

myTree.preorder(root)
print()
