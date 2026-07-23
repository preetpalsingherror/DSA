class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def INSERT_AT_BEGIN(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def INSERT_AT_END(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    # Insert at Position
    def INSERT_AT_POSITION(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                print("Element is not in this linkedlist")
                return
        new_node.next = temp.next
        temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="--aayehaye-->")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.INSERT_AT_END(10)
ll.INSERT_AT_END(20)
ll.INSERT_AT_END(30)
ll.INSERT_AT_BEGIN(5)
ll.display()  # Output: 5--aayehaye-->10--aayehaye-->20--aayehaye-->30--aayehaye-->None

ll.INSERT_AT_POSITION(25, 3)
ll.display()  # Output: 5--aayehaye-->10--aayehaye-->20--aayehaye-->25--aayehaye-->30--aayehaye-->None

