# define a tree

class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self,root, size):
        self.root = root
        self.size = size
    