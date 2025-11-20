# 主要考察排序函数 sorted

a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = int(input("请输入第三个数："))


list1 = [a, b, c]
# 正序排列
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)

print(list2)
print(list3)
