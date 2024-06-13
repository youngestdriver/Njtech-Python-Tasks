'''
定义函数f, 计算一个给定正整数的各位数字之和。输入函数调用语句进行测试。
样例: 
输入: f(324)
输出: 324的各位数字之和是9
'''
def f(num):
    sum1=0
    for i in str(num):
        sum1+=int(i)
    return [num,sum1]

a=eval(input())
print("{}的各位数字之和是{}".format(a[0],a[1]))
