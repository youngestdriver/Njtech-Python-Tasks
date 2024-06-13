'''
2、设计一个函数，判断指定的一个正整数是否为完数，并调用该函数进行测试。要求如下：
函数名：isWs
返回值：是完数返回True，不是完数返回False
样例1：
输入：
isWs(6)
输出：
6是完数
样例2：
输入：
isWs(7)
输出：
7不是完数
'''
"""
    This function checks if a given positive integer (n) is a perfect number.
    A perfect number is equal to the sum of its proper divisors, excluding itself.
    
    Args:
    n (int): The positive integer to check.
    
    Returns:
    bool: True if n is a perfect number, False otherwise.
"""
def isWs(num):
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    if sum_factors == num:
        print("{}是完数".format(num))
    else:
        print("{}不是完数".format(num))

eval(input())


# # Testing the isWs function
# test_numbers = [6, 28, 496, 8128, 33550336, 10, 12, 18]  # Includes both perfect and non-perfect numbers

# print("Testing the isWs function:")
# for number in test_numbers:
#     print(f"Is {number} a perfect number? {isWs(number)}")
