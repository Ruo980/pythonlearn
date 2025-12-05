string: str = input("请输入字符串：")

char = 0
number = 0
space = 0
other = 0

for i in string:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        number+=1
    elif i.isspace():
        space+=1
    else:
        print(" ")

print(f"字符串中的字符数为{char}")