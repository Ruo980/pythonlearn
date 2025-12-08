# 列表的复制分为浅拷贝和深拷贝
lst: list[int] = [1, 2, 3, 4]
list1: list[int] = lst
lst[0] = 5
print(list1)

import copy

list2: list[int] = copy.copy(lst)
lst[0] = 5
print(list2)
