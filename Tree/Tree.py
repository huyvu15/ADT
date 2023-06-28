# define a tree
import Queue as Que

class Node:
    def __init__(self,value, left = None, right = None):
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
        
    def glue(self, node, leftNode, rightNode ): # gán 2 cây con vào con trái, con phải của node
        '''
        khi gọi hàm chú ý là phải truyền dữ liệu là Node(...), Node(...), Node(...)
        '''
        node.left = leftNode
        node.right = rightNode
           
        
    def printTree(self, level=0):
        print("    " * level + str(self.value))
        if self.left:
            self.left.printTree(level + 1)
        if self.right:
            self.right.printTree(level + 1)


class Tree:
    def __init__(self,root, size):
        self.root = root
        self.size = size

def mergeTrees(t1, t2): # ghép 2 cây không theo node
    if not t1:
        return t2
    if not t2:
        return t1

    merged_value = t1.value + t2.value
    merged_left = mergeTrees(t1.left, t2.left)
    merged_right = mergeTrees(t1.right, t2.right)

    merged_tree = Node(merged_value, merged_left, merged_right)
    return merged_tree

# thuật toán duyệt cây
# DFS
def preOrder(p):
    '''
    thuật toán duyệt trước DFS
    p là kiểu node nên chú ý khi truyền vào Node(...)'''
    if p != None:
        print(p.value) # có thể thay = f(p) là 1 thao tác nào đấy để thay thế
        preOrder(p.left)
        preOrder(p.right)
        
def BFS(p):
    '''
    thuật toán duyệt trước BFS
    p là kiểu node nên chú ý khi truyền vào Node(...)
    '''
    q = Que.Queue()
    q.enqueue(p)
    while not q.isEmpty():
        curNode = q.dequeue()
        # duyệt Node đó
        print(curNode.value)
        if curNode.left != None:
            q.enqueue(curNode.left)
        if curNode.right != None:
            q.enqueue(curNode.right)    



       
# ở đây chỉ tạo theo dạng node dạng tree tương tự(chỉ cần bỏ phần comment)

# Ví dụ tạo 1 cây t root = 5
"""
    t.addLeftChild(t.root, 4)
    t.addRightChild(t.root.left, 6)
    t.addLeftChild(t.root.left.right, 7)
    t.addLeftChild(t.root.left.right, 8)  
"""

# khởi tạo
t = Node(5)
t.addLeftChild(t, 4)
t.addRightChild(t.left, 6)
t.addLeftChild(t.left.right, 7)
t.addRightChild(t.left.right, 8)
# t.addRightChild(t.left.right, 9) # dòng này sai vì phải là t.left.right.right

t.printTree()


# Tạo cây thứ nhất
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)
t1.left.left = Node(4)
t1.left.right = Node(5)

# Tạo cây thứ hai
t2 = Node(6)
t2.left = Node(7)
t2.right = Node(8)
t2.left.left = Node(9)
t2.left.right = Node(10)

# Ghép hai cây
merged_tree = mergeTrees(t1, t2) 

print("ghép cây 1 với cây 2:")

# In cây ghép không qua Node
merged_tree.printTree()

print("Cây được duyệt bằng DFS:")
preOrder(merged_tree)

print("Cây được duyệt bằng BFS:")
BFS(merged_tree)