class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(40)
root.right = Node(30)
root.left.left = Node(20)
root.left.right = Node(10)


def inorder(node):   # Left -> Root -> Right
    if node is None:
        return
    inorder(node.left)
    print(node.data , end = ' ')
    inorder(node.right)


def preorder(node):  # Root -> Left -> Right
    if node is None:
        return
    print(node.data , end = ' ')
    preorder(node.left)
    preorder(node.right)


def postorder(node): # Left -> Right -> Root
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data , end = ' ')

print("Inorder (Sorted order for BST):")
inorder(root)  # Output: 40 20 50 10 30
print("\nPreorder (Root first):")
preorder(root) # Output: 10 20 40 50 30
print("\nPostorder (Children first):")
postorder(root) # Output: 40 50 20 30 10