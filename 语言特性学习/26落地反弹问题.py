# 初始高度
n: int = 100
count: int = 0
l: list[int] = []  # 每次弹跳的长度

while count < 10:
    # 区分第一次和第10次的区别
    if count == 0:
        l.append(n)
    else:
        l.append(n * 2)
    count += 1
    n /= 2

print(l)
print(sum(l)) # 10 次的路径总长度
print(l[-1]/2) # 第 10 次的弹跳高度

# python 列表的使用：初始化l: list[int] = []；添加元素 append(n)；求和 sum(l)；求最后一个元素 l[-1]；