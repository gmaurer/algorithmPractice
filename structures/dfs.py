
def preorder_binary_depth_first_search(root):
    if root:
        print(root.value, end=" ")
        preorder_binary_depth_first_search(root.left)
        preorder_binary_depth_first_search(root.right)

def postorder_binary_depth_first_search(root):
    if root:
        postorder_binary_depth_first_search(root.left)
        postorder_binary_depth_first_search(root.right)
        print(root.value, end=" ")

def inorder_binary_depth_first_search(root):
    if root:
        inorder_binary_depth_first_search(root.left)
        print(root.value, end=" ")
        inorder_binary_depth_first_search(root.right)
