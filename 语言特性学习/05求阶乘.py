# 方法一：遍历
sum = 1
num = 5
for i in range(2, num + 1):
    sum *= i

print(sum)

# 方法二：递归
def fun(n):
    if n==0:
        return 1
    else:
        sum = n * fun(n-1)
    return sum

print(fun(num))
