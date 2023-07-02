# Lý thuyết 
- Là cây nhị phân chưa hoàn chỉnh

- min -heap, max -heap

(k, v): k- khóa, v-value

$\rightarrow$ theo mức độ ưu tiên

> Các phương thức
- Thêm 1 nút

- Xóa 1 phần tử (chỉ xóa tại gốc)

- Xây dựng 1 đống nhị phân từ dãy khóa k


> Xây dựng 1 đống nhị phân từ 1 đống phần tử
2   3   1   6   4   5   8(n = 7)

Sắp xếp vun đống - heap sort

B1: xây dựng đống nhị phân cực tiểu biểu diễn các phần tử đã cho (cần sắp xếp)

Chi phí: O(n)

Mảng cần tìm |0|1|5|2|4|9|8|6|3|10|

B2: Gọi hàm / phương thức remove() n lần

$\rightarrow$ Chi phí O(nlogn)

Sau khi gọi hàm remove()

Lời gọi remove

|1|2|5|3|4|9|8|6|10|0|

