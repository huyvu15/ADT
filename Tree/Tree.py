# define a tree

class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def hasLeftChile(self, p):
        pass
    
    def hasRightChile(self, p):
        pass
    
    def addLeftChild(self, p, item):
        pass
    
    def addRightChild(self, p, item):
        pass

class Tree:
    def __init__(self,root, size):
        self.root = root
        self.size = size
    