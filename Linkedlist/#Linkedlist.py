#Linkedlist
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# ví dụ duyệt danh sách:
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    return ans
# có thể duyệt bằng đệ quy như sau:\
'''    
def get_sum(head):
    if not head:
        return 0
    return head.val + get_sum(head.next)
'''
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three

head = one



print("Phẩn tử head",head.val)
print("Phần tử tiếp sau đầu",head.next.val)
print(head.next.next.val)
print("Tổng các phần tử của linkedlist",get_sum(head))
'''
phép gán:
ptr = head
head = head.next
head = None
'''