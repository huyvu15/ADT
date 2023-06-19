# #Linkedlist_set
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
    
# n = int(input())
# print(n, list)


# one = Node(1)
# two = Node(2)
# three = Node(3)

# one.next = two
# two.next = three

# head = one
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
        

#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

# n = int(input())
# linked_list = LinkedList()
# list1 = list(map(int, input().split()))

# for i in list1:
#     LinkedList.insert(int(i))

# # In danh sach lien ket
# current = linked_list.head
# while current:
#     print(current.data, end=" ")
#     current = current.next
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

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

n = int(input())
linked_list = LinkedList()
list1 = list(map(int, input().split()))

for i in list1:
    linked_list.insert(i)

linked_list.traverse()

