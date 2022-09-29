class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def printlist(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete_by_value(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            return
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
            
