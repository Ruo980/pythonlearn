from re import A


def prime(m):
    """判断 n 是否为素数

    Args:
        m (int): 整数
    """
    flag = True  # 默认是素数
    for i in range(2, m):
        if m % i == 0:
            flag = False
            break
    return flag


a = int(input("请输入区间中的第一个数:"))
b = int(input("请输入区间中的第二个数:"))

list = []
for i in range(a, b + 1):
    if prime(i):
        list.append(i)

print(list)
