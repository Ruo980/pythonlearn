# 列表的复制分为浅拷贝和深拷贝
list = [1,2,3,4]
list1 = list
list[0] = 5
print(list1)

import copy

list2 = copy.copy(list)
list[0] = 5
print(list2)