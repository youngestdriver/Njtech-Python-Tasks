'''
二、试编写程序，完成以下功能：
1、定义一个函数(函数名为f)：计算给定的两个正整数的最小公倍数
2、根据用户输入的函数调用表达式直接输出结果，具体输入输出格式见样例。（10分）

输入样例：
f(9,6)

输出样例：
18
'''

def f(m,n):                     #定义函数，计算给定的两个正整数的最小公倍数，并将其返回
    if m>n:
        m,n=n,m                 #交换m和n的值，使n的值大于m的值
    i=n
    while True:
        if i%m==0 and i%n==0:   #判断当前i的值是否是m和n的公倍数
            return i#返回当前i的值
        i+=1#计算i的下一个取值

result=eval(input())            #输入函数调用表达式用于得到结果
print(result)
