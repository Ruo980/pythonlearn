a: list[int] = []
# 构建二维矩阵切片
for i in range(0, 3):
    a.append([])
    for j in range(0, 3):
        k: int = int(input("请输入元素:"))
        a[i].append(k)

print(a)

sum: int = 0
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            sum += a[i][j]
print(sum)
