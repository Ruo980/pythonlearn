# 根据输入的单词判断是星期几
# 星期一 Monday、星期二 Tuesday、星期三 Wednesday、星期四 Thursday、星期五 Friday、星期六 Saturday、星期日 Sunday
a = input("请输入第一个星期单词:")

if a == "Monday":
    print("是周一")
elif a == "Tuesday":
    print("是周二")
elif a == "Wednesday":
    print("是周三")
elif a == "Thursday":
    print("是周四")
elif a == "Friday":
    print("是周五")
elif a == "Saturday":
    print("是周六")
elif a == "Sunday":
    print("是周日")
else:
    print("输入错误")
