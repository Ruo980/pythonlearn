L:list[int] = []
for i in range(1, 100):  # range 左闭右开
    if i % 2 != 0:
        L.append(i)  # 对象方法

print(L)
