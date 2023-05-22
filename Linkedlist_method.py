# define a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# define Linkedlist
class LinkedList:
    def __init__(self):
        self.head = None
    
    # add a elements into first posstion
    def append_First(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    
    # add a elements into last posstion
    def Append(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return 1
        
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        
        cur_node.next = new_node
    
    # insert a elements into any possition
    def insert(self, p, val):
        new_node = Node(val)
        
        if p == 0:
            new_node.next = self.head
            self.head = new_node
        
        # new_node.next = new_node
        cur_node =  self.head
        
        # lấy ra node hiện tại theo vị trí p
        count = 0
        while count < p-1 and cur_node.next:
            cur_node = cur_node.next
            count+=1
        
        new_node.next = cur_node.next    
        cur_node.next = new_node
        
        '''Truyền vào gì
        của cô là truyền vào giá trị và node hiện tại
        insert(val, node cur_node(vị trí))
        '''
    # có thể thêm hàm này thay cho insert theo cách cô  
        
    def remote_First(self):
        self.head = self.head.next
    
    def remote_Last(self):
        # if this.next == None:
        #     this = None
        #     return 
        
        cur_Node = self.head
        while cur_Node.next.next is not None :
            cur_Node = cur_Node.next 
        cur_Node.next = None
    
    def remote(self, p):
        cur_Node = self.head
        count = 0
        while count < p-1 and cur_Node.next != None:
            cur_Node = cur_Node.next
            count +=1
        
        cur_Node.next = cur_Node.next.next
                
        
        ''' đoạn này theo cô là xóa 1 phần tử sau 1 node nào đó
        giá trị truyền vào hàm sẽ là 1 Node có trong LinkedList
        còn ở đây ta chỉ xét xóa tại 1 ví trí nào đó thôi
        '''
        pass
    
    # In ra danh sách liên kết đơn
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="")
            if current_node.next is not None:
                print("->", end="")
            current_node = current_node.next
        print(" ")

        
# b = LinkedList()
# b.append_First(1)
# b.append_First(2)
# b.Append(1)
# b.insert(1, 2)
# b.print_list()

n = int(input())
linked_list = LinkedList()
list1 = list(map(int, input().split()))
# p, val = list(map(int, input().split()))
# k = int(input())

for i in list1:
    linked_list.Append(i)


# linked_list.insert(p, val)
# linked_list.remote_First()
# linked_list.remote_Last()
# linked_list.remote(k)
linked_list.print_list()
    
        