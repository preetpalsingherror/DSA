def INSERT_AT_end(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    temp = self.head
    while temp.next is not None:
        temp = temp.next


    temp.next = new_node
