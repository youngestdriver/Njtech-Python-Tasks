x=eval(input())
y=eval(input())
if x>0 and y>0:
    print("第一象限")
elif x>0 and y<0:
    print("第四象限")
elif x<0 and y>0:
    print("第二象限")
else x<0 and y<0:
    print("第三象限")