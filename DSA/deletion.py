class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def INSERT_AT_END(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def DISPLAY(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def DELETE(self, data):
        # Case 1: Empty list
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # Case 2: Delete head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Case 3: Walk and delete from middle/end
        temp = self.head
        while temp.next is not None and temp.next.data != data:
            temp = temp.next

        if temp.next is None:
            print("Element not found.")
            return

        temp.next = temp.next.next

# ---- Testing ----
ll = LinkedList()
ll.INSERT_AT_END(10)
ll.INSERT_AT_END(20)
ll.INSERT_AT_END(30)
ll.INSERT_AT_END(40)

print("Original List:")
ll.DISPLAY()  # 10 -> 20 -> 30 -> 40 -> None

ll.DELETE(20)
print("After deleting 20:")
ll.DISPLAY()  # 10 -> 30 -> 40 -> None

ll.DELETE(10)
print("After deleting 10:")
ll.DISPLAY()  # 30 -> 40 -> None

ll.DELETE(100)
print("After trying to delete 100:")
ll.DISPLAY()  # 30 -> 40 -> None (with "Element not found" message)xt == temp.next.next

