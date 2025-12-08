# 输入年月日判断是本年的第几天
import datetime

year, month, day = map(int, input().split(" "))
yuandan: datetime.datetime = datetime.datetime(year, 1, 1)
now: datetime.datetime = datetime.datetime(year, month, day)

days: int = (now - yuandan).days + 1
print(days)
