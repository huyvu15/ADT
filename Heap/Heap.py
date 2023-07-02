import math

def swap(a, b):
    return b, a    

class Heap:
    def __init__(self, key, left, rigth) -> None:
        self.key = key
        self.left = left
        self.right = rigth
    
    # def add(self, key):
        
class Heap:
    def __init__(self, key, size):
        self.key = key
        self.size = size
    
    def add(self, key):
        key[self.size] = key
        childId = self.size
        parentID = math.floor((childId/2)-1)   
        while parentID >= 0 and key[childId] < key[parentID]:
            swap(parentID, childId) # hoán đổi 2 phần tử mảng
            childId = parentID
            parentID = math.floor((childId-1)/2)
            
        size +=1

    def remove(self):
        tmp = self.key[0]
        self.key = self.key[self.size-1] # chép giá trị cuối lên đỉnh
        parentID = 0
        while parentID <= (self.size -2)/2:
            leftChild = 2*parentID +1
            rightChild = 2*parentID +2
            
            # còn phải sửa lệnh if này
            if leftChild < rightChild:
                pass
        self.size +=1
        return # trả về heap
    