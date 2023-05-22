class Queue:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.elems = []
        
    def enqueue(self,item):
        self.elems.append(item)
        self.tail += 1
    
    def dequeue(self):
        if self.isEmpty():
            return None
        out = self.elems[self.head]
        self.head +=1
        return out
    
    def isEmpty(self):
        return self.head == self.tail
        
    def top(self):
        if self.isEmpty():
            return None
        return self.elems[self.head] 
    def display(self):
        print(self.elems[self.head::])
        
    def size(self):
        return len(self.elems)   
    
q = Queue()
# q.cre_Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)    
q.enqueue(4)
q.enqueue(5)

q.display()

# print(q.dequeue())
print(q.dequeue())

print("After removing an element")  
q.display()
print(q.top())