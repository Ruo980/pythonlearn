# 输入年月日判断是本年的第几天
import datetime

year,month,day = map(int,input().split(" "))
yuandan = datetime.datetime(year,1,1)
now = datetime.datetime(year,month,day)

days = (now-yuandan).days+1
print(days)