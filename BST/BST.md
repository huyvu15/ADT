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

# Cây cân bằng
- Là cây tìm kiếm nhị phân có độ chênh lệch chiều cao của cây con có gốc ở p 

|h(p.left) - h(p.right)| <= 1

- Tính chất: cây cb có kích thước n có chiều cao là  clogn

CM: Giả sử cây cần bằn chiều cao h có kích thước là T(h)

$\rightarrow$ T(h) <= 1 + 2T(h-1)

T(1) = 1

T(2) = 3



