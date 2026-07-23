class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("STACK IS EMPTY")
            return
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
            return
        return self.head.data
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())   # 30
print(s.pop())    # 30
print(s.pop())    # 20
print(s.pop())    # 10
print(s.pop())    # STACK IS EMPTY