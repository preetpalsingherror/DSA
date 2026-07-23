class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST: 
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  
        
        if self.root is None:
            self.root = new_node
            return
        
        temp = self.root 
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.data, end=" ")
        self._inorder(node.right)

# --- Testing ---
tree = BST()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)

print("Inorder Traversal (Sorted):")
tree.inorder()  # Output: 20 30 40 50 70