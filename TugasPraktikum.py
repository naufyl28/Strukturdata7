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
        if node.next.data == data:
            self.head = node.next
            return
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
            
    def delete_duplicates(self):
        node = self.head
        seen = set()
        while node:
            if node.data in seen:
                self.delete_by_value(node.data)
            else:
                seen.add(node.data)
            node = node.next
    def switch_tail_to_head(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next.next = self.head
        self.head = node.next
        node.next = None
        
 llist = LinkedList()
print("Data awal")
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(4)
llist.insert(1)
llist.printlist()
print("Data setelah dihapus")
llist.delete_by_value(3)
llist.printlist()
print("Data setelah dihapus duplikat")
llist.delete_duplicates()
llist.printlist()
print("Data setelah ditukar")
llist.switch_tail_to_head()
llist.printlist()

        
        
            
