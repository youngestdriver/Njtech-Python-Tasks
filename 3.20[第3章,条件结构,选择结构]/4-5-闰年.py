a=int(input())
if a%400==0:
    print(a,end="年是闰年")
elif a%4==0 and a%100!=0:
    print(a,end="年是闰年")
else:
    print(a,end="年不是闰年")
