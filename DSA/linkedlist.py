class Node:
    def __init__ (self , data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    

    #insertion of element at the begining 
    def InsertATbeg(Self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insertion at the  end 
    def InsertionATend(self,data):
        new_node = Node(data)
        if self.head is None:
            temp = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    #insert at position
    def InsertATpos(self,data,position):
        if position == 0: #insert at begining 
            new_node.next = self.head
            self.head = new_node
            return
        #walk it baby 
        temp = self.head #creating new variable temp which will walk to the postion we want
        if i in range(position -1):
            temp = temp.next
            if temp is none:
                print("element is not in our linkedlist")
                return
            
        new_node.next = temp.next
        temp.next = new_node
            

            
