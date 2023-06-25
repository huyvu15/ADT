# Tree
## Khái niệm cơ bản
> Cây

- Gốc (là 1 nút đặc biệt)

- Nút (node):

+ lá

+ nhánh

- Cạnh

- Cây con

> Nút
- Bậc (degree): số nút con của chính nó

- Mức (level): 

+ Nút gốc: mức 0

+ Nút (p) = mức(node cha) + 1 (Đệ quy)

# Thuật toán duyệt cây

## DFS: 

Duyệt cây theo chiều sâu

> preOrder: duyệt trước

Chú ý không dùng kiểu dữ liệu Tree do không dùng được đệ quy

Ví dụ: preOrder(Tree.root) // in toàn bộ cây
       preOrder(Tree.root.right) // in toàn bộ nhánh con bên phải


> inOrder: duyệt trong

> duyệt sau

