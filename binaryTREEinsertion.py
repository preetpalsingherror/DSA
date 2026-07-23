class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # 1. Create the new node
        new_node = Node(data)
        
        # 2. If tree is empty, make it the root
        if self.root is None:
            # TODO: Set self.root to new_node
            self.root = new_node
            return
        
        # 3. Start walking from the root
        temp = self.root
        while True:
            # If data is smaller, go LEFT
            if data < temp.data:
                # TODO: Check if temp.left is None
                # If it is None, attach new_node here and return
                # Else, move temp to temp.left
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
                pass
            # If data is bigger, go RIGHT
            else:
                # TODO: Check if temp.right is None
                # If it is None, attach new_node here and return
                # Else, move temp to temp.right
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right
                pass

    # Inorder traversal to check if our tree is correct (it will print sorted order)
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.data, end=" ")
        self._inorder(node.right)
# Test
tree = BST()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)

print("Inorder Traversal (Sorted):")
tree.inorder()  # Output: 20 30 40 50 70