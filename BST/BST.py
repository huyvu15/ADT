class BST:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
    
    def Searchkey(self, node, key_to_Find):
        if node == None: return None
        if node.key == key_to_Find: return node
        if key_to_Find < node.key: return self.Searchkey(node.left, key_to_Find)
        if key_to_Find > node.key: return self.Searchkey(node.right, key_to_Find)
    
    def min(self, p):
        # tìm node chứa khóa bé nhất trên cây có gốc ở node # null
        if p is None: return None
        while p.left != None :
            p = p.left
        return p
    # do truyền tham chiếu  node bị thay đổi
    
    def max(self, p):
        # tìm node chứa khóa bé nhất trên cây có gốc ở node # null
        if p is None: return None
        while p.right!= None :
            p = p.right
        return p
    
    # hàm next này để từ sửa chỗ gắn tmp
    def next(self, p): # tìm các nút  tìm sau
        if p.right!= None: return min(p.right)
        else:
            tmp = self
        while tmp != p.key:
            if tmp.key > p.key:
                s = tmp
                tmp = tmp.left
            else:
                tmp = tmp.right
        return s
    
    # viết tương tự đối với tìm các nút liền trước
    
    def add(self, value): 
        v = self.search(value)
        if value < v.key:
            new_bst = BST(value)
            v.left = new_bst
        elif value > v.key:
            pass
        else:
            print("Trên cây có rồi")
        
    def Search(self,node, value):
        if node == None: return None
        if node.key == value: return None
        if node.left != None and value > node.key: return self.Search(node.left, value)
        if node.right != None and value > node.key: return self.Search(node.right, value)
        return None
    
    # có thể thêm hàm search này vào hàm add cho gọn hơn