class bst:
    def __init__(self):
        self.root = None
def insert(self,data):
    if self.root is None:
        self.root  = new_node
        return
    temp  = temp.root
    while True:

        if data < temp.data:
            if temp.left is None:
                temp.left  = new_node
                return
            else:
                temp = temp.left

        else:
            if temp.right is None:
                temp.right = new_node
                return
            else:
                temp = temp.right
            pass
