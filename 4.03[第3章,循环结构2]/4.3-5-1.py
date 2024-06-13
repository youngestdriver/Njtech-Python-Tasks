b=int(input())
a=int(input())

while a!=b:
    if a>b:
        print("您猜大了！")
    else:
        print("您猜小了！")
    a=int(input())
print("您猜对了！")
