import math
a=eval(input("请输入三角形第一条边的长度："))
b=eval(input("请输入三角形第二条边的长度："))
c=eval(input("请输入三角形第三条边的长度："))
l=(a+b+c)/2
S=math.sqrt(l*(l-a)*(l-b)*(l-c))

print("三角形的面积是：{}".format(S))