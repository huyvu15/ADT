# cài đặt các thuật toán sắp xếp bình phương
def swap(a, b):
    return b, a
    
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = swap(a[j], a[j+1])
    
    print(a)

def select_sort(a):
    n = len(a)
    for i in range(n-2):
        id_min = i
        for j in range(i+1, n-1):
            if a[j] < a[id_min]:
                a[j], a[id_min] = swap(a[j], a[id_min])
    print(a)

def insert_sort(a):
    n = len(a)
    for i in range(n-1):
        val = a[i]
        j = i
        while j > 0 and a[j] > val:
            a[j+1] = a[j]
            j = j - 1
        a[j] = val
    print(a)

a = list(map(int, input().split()))
bubble_sort(a)
select_sort(a)
insert_sort(a)
