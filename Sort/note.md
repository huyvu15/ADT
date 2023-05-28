# Đánh giá sort algorithm
Tiêu chí đánh giá:

> Độ phức tạp (1)

> Số lần đổi chỗ - Độ phức tạp đổi chỗ (2)

> Bộ nhớ  : có dùng thêm bộ nhớ không (3)
- In-place : sắp xếp tại chỗ
- not in-place : ko tại chỗ
> Tính ổn định : thứ tự của các phần tử trùng nhau sau khi sắp xếp không đổi (4)
- Ổn định
- Không ổn định

# Thuật toán có độ phức tạp bình phương

## Bubble sort
> (1) $O(n^2)$

> (2) Độ phức tạp đổi chỗ $O(n^2)$

> (3) In-place

> (4) Ổn định

## Select sort
> (1) $O(n^2)$

> (2) $O(n)$

> (3) in-place

> (4) Ko ổn định

Ví dụ minh họa:
- Ex: Sắp xếp dãy: $5^{1}$, 3, $5^{2}$, 2
- result: 2, 3, $5^{2}$, $5^{1}$

## Insert sort
> (1) $O(n^2)$

> (2) $O(n^2)$

> (3) In-place

> (4) Ổn định