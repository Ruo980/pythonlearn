import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"三角形面积：{s}")
print("三角形的面积是%.2f" % s) # % 是告诉 python 解释器后面的内容是用来格式化前面字符串的占位符的
