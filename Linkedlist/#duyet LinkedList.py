#duyet LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def replace_value(self, a, b):
        cur_node = self.head
        
        while cur_node is not None:
            if cur_node.data == a:
                cur_node.data = b

            cur_node = cur_node.next
            
    # In ra danh sách liên kết đơn
    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()              
    
n = int(input())
linked_list = LinkedList()
list1 = list(map(int, input().split()))
p, val = list(map(int, input().split()))
for i in list1:
    linked_list.insert(i)
    
linked_list.replace_value(p, val)
linked_list.print_list()





