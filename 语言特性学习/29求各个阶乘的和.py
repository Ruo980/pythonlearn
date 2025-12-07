# 求 1 + 2! + 3! +4!
# 阶乘函数 math.
import math

sum: int = 0
for i in range(1, 21):
    sum += math.factorial(i)
print(sum)
