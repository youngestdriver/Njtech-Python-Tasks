import math
r=eval(input("请输入球的半径："))
S=4*math.pi*r**2
V=(4/3)*math.pi*r**3
print("球的表面积为：{}".format(S))
print("球的体积为：{}".format(V))