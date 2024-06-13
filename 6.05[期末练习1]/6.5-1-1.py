'''
假设有一只球, 从一百米高空坠落, 每次反弹回原来一半的高度。
试编写程序, 计算经过n次反弹以后, 小球总共经过了多少米? 
样例：
输入：
1
输出：
150
'''
# def f(n):
#     h=100
#     len=0
#     for i in range(n):
#             len+=(h*1.5)
#             h=h//2
#     return(len)

# print(f(int(input())))
h=100
len=0
n=int(input())
for i in range (n):
    len=len+h*1.5
    h=h/2
print(len)