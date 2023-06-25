# define a tree

class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def hasLeftChile(self, p):
        if p.left == None: return False
        return True
    
    def hasRightChile(self, p):
        if p.right == None: return False
        return True
    
    def addLeftChild(self, p, item):
        if self.hasLeftChile(p):
            print("Không thêm được nữa")
            return 1
        newNode = Node(item)
        p.left = newNode
        # size +=1 
            
    def addRightChild(self, p, item):
        if self.hasRightChile(p):
            print("Không thêm được nữa")
            return 1
        newNode = Node(item)
        p.right = newNode
        # size +=1

class Tree:
    def __init__(self,root, size):
        self.root = root
        self.size = size
        
        