s=input()
if s.isdigit()==True:
    print("输入的是数字")
elif s.encode('utf-8').isalpha()==True:
    print("输入的是英文字母")
else:
    print("输入的是其他字符")