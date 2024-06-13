'''
三、试编写程序，实现以下功能：
1. 定义一个函数(函数名为f)：计算给定列表中的所有素数之和。
假设列表中的元素均为正整数。
2. 根据用户输入的函数调用表达式，计算结果并将其输出。
具体输入输出格式见样例。（10分）

输入样例：
f([2,3,4,5,6])

输出样例：
10
'''
def prime(n):  # 定义函数prime，用于判断给定的一个正整数是否为素数，是则返回True，不是则返回False
    for i in range(2, int(n**0.5) + 1):  # 遍历从2到sqrt(n)的所有整数
        if n % i == 0:  # 如果n能被i整除，则n不是素数
            return False
    return True  # 如果没有找到任何能整除n的数，则n是素数

def f(lst):  # 定义一个函数，计算给定列表中的所有素数之和
    s = 0
    for num in lst:  # 对列表lst进行遍历
        if prime(num):  # 调用prime函数对当前列表元素是否为素数进行判断
            s += num  # 如果是素数，累加到s上
    return s  # 返回和变量

result = eval(input())
print(result)  # 输出结果