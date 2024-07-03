'''
3、设计一个函数，判断指定的一个正整数是否为素数，并调用该函数进行测试。要求如下：
函数名：isPrime
返回值：是素数返回True，不是素数返回False
样例1：
输入：
isPrime(7)
输出：
7是素数
样例2：
输入：
isPrime(6)
输出：
6不是素数
'''
def isPrime(num):
    if num < 2:
        print("{}不是素数".format(num))
    return False        #应该在循环外部！！！！！
    for i in range(2, num+ 1):
        if num % i == 0:
            print("{}不是素数".format(num))
            break
        print("{}是素数".format(num))

eval(input())
'''
print不能终止函数，但return可以！！
'''