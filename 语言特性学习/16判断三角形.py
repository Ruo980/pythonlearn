a = int(input())
b = int(input())
c = int(input())
# 三个正整数满足如下条件：任意两边之和大于第三边
if a<=0 or b<0 or c<0:
    print("输入数据不合法")
if a+b>c and a+c>b and b+c>a:
    print("这三条边可以是三角形的边长")
else:
    print("这三条边不可以是三角形的边长")