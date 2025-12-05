# 方法一：递归法
def fib(b):
    if b ==1 or b ==2:
        return 1
    else:
        return fib(b-1)+fib(b-2)

a = int(input("请输入一个数:"))
print(fib(a))

# 方法二：非递归方法
fibs: list[int] = [1,1]
for i in range(2,a+1):
    fibs.append(fibs[i-1]+fibs[i-2])

print(fibs[a-1])