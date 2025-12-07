# 函数定义学习
# 前一个人比后一个人小 2 岁，给出第一个人年龄，求最后一人的年龄
# 使用递归求解
def func(n:int)->int:
    if n==1:
        return 10
    else:
        return func(n-1)+2

print(func(5))