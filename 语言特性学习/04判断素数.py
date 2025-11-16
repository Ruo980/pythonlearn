# 素数：只能被1和它本身整除
num = 20
flag = True
for i in range(2, num // 2):  # // 表示整数除法
    if num % i == 0:
        flag = False
        break

if flag:
    print("素数")
else:
    print("合数")
