import math
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
    
    
def merge_sort(a, l, r):
    if r > l:
        mid = math.floor((l + r) / 2)
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, r, mid)

def merge(a, l, r, mid):
    n1 = mid - l + 1
    n2 = r - mid
    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = a[l + i]

    for j in range(n2):
        right[j] = a[mid + 1 + j]

    i = 0
    j = 0
    merge_index = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            a[merge_index] = left[i]
            i += 1
        else:
            a[merge_index] = right[j]
            j += 1
        merge_index += 1

    while i < n1:
        a[merge_index] = left[i]
        i += 1
        merge_index += 1

    while j < n2:
        a[merge_index] = right[j]
        j += 1
        merge_index += 1



def quick_sort(a, l, r):
    if l < r:
        i = pattion(a, l, r)
        quick_sort(a, l, i -1)
        quick_sort(a, i+1, r)

def pattion(a, l, r):
    pivot = a[r]
    i = l
    for j in range(l, len(a)):
        if a[j] < pivot:
            a[i], a[j] = swap(a[i], a[j])
            i = i + 1
    a[i], a[r] = swap(a[i], a[r])
    return i




# a = list(map(int, input().split()))
a = [7, 2, 1, 6, 8, 5, 3, 4]
print("Result:")
bubble_sort(a)
select_sort(a)
insert_sort(a)
quick_sort(a, 0, len(a) - 1)
print(a)
merge_sort(a, 0, len(a) - 1)
print(a)


