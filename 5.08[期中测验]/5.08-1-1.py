'''
编写程序，输出给定范围内既能被7整除又不能被5整除的所有整数。
范围的起始值(整数)和终止值(整数)由用户输入。
样例：
输入：
1
100
输出：
7,14,21,28,42,49,56,63,77,84,91,98
'''
a=int(input())
b=int(input())
lst=[]
for i in range(a,b):
    if i%7==0 and i%5!=0:
        lst.append(str(i))
print(",".join(lst))