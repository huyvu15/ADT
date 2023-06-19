class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def appendFirst(self, value):
        a = Node(value)
        a.next = self.head
        self.head = a
        
    def insert(self, value, curNode):
        a = Node(value)
        a.next = curNode.next
        curNode.next = a
        
    def __str__(self):
        if self.head is None:
            return "Empty List"
        else:
            current_node = self.head
            output = "LinkedList:\n["
            while current_node is not None:
                output += str(current_node.data)
                if current_node.next is not None:
                    output += ", "
                current_node = current_node.next
            return output+"]"
        

a =Node(1, 2)        
b = LinkedList()
b.appendFirst(1)
b.appendFirst(1)
b.appendFirst(1)
b.insert(4, 2)
print(b)

# Kiểm tra tính đúng đắn của biểu thức
