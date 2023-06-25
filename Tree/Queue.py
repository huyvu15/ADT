# cài đặt hàng đợi bằng linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def enqueue(self, item):
        node = Node(item)
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count +=1
        
    def dequeue(self):
        if self.isEmpty():
            return None
        out = self.head.data
        self.head = self.head.next
        self.count -=1
        return out
    
    def top(self):
        return self.head.data
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="")
            if current_node.next is not None:
                print("->", end="")
            current_node = current_node.next
        print(" ")

        
        
    
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# print(q.dequeue())

# print(q.top())
# q.display()
        
        