# 2/1 + 3/2 + 5/3 + 8/5... 即分子是前一项的分母，分母为前一项的分子分母和
# 求第 20 项之和
up: int = 2
down: int = 1
sum: float = 0.0
a: float = 0.0
for i in range(20):
    sum += up / down
    a = up
    up = up + down
    down = a

print(sum)
