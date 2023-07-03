# Lý thuyết
Cây tìm kiếm nhị phân, ký hiệu: BST

Là 1 cây nhị phân có 1 quan hệ R sao cho nút con trái có mối quan hệ R với nút cha

> con trái R cha

> cha R con phải

- Để tìm kiếm lưu trữ nhiều

- Thao tác tìm kiếm

Các phương thức:
- Min(), Max()

- Searchkey()

- next(p)

- add()

- remove()

- search

## Tất cả thao tác đều có độ phức tạp là O(h) = O(n)

# Cây cân bằng (Cây AVL)
- Là cây tìm kiếm nhị phân có độ chênh lệch chiều cao của cây con có gốc ở p 

- Đảm bảo cho các chi phí trên cây tìm kiếm nhị phân là tối thiểu

|h(p.left) - h(p.right)| <= 1

- Tính chất: cây cb có kích thước n có chiều cao là  clogn

CM: Giả sử cây cần bằn chiều cao h có kích thước là T(h)

$\rightarrow$ T(h) <= 1 + 2T(h-1)    (1)

T(1) = 1

T(2) = 3

Cây cb thêm 1 nút có thể mất đi tính cân bằng. Làm thế nào để khi thêm vào 1 node thì cây thu đc vẫn là cây cb

Ví dụ: [15, 10, 5, 20, 18, 30, 40, 35, 25, 28]

B1: $a_0$ = 15

B2: $a_1$ = 10

B3: $a_2$ = 5
cây mất tính cb do ko thỏa mãn công thức (1)

cần tái cân bằng cây

B4: $a_4$ = 20
cây ko mất tính cân bằng

B5: $a_5$ =18
cây mất tính cb

B6, 7: $a_6$ = 30, $a_7$ = 40







