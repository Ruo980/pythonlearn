import math

a = int(input("请输入第一个直角边的长度:"))
b = int(input("请输入第二个直角边的长度:"))

m = a * a + b * b
c = math.sqrt(m)

print(f"第三个直角边的长度为{c}")
