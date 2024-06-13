'''
1、设计一个函数，判断指定的一个三位正整数是否为水仙花数，并调用该函数进行测试。要求如下：
函数名：isSxh
返回值：是水仙花数返回True，不是水仙花数返回False
样例1：
输入：
isSxh(153)
输出：
153是水仙花数
样例2：
输入：
isSxh(103)
输出：
103不是水仙花数
'''
def isSxh(number):
    # Ensure the number is a three-digit integer
    if not (100 <= number <= 999):
        raise ValueError("The number must be a three-digit integer")
    
    # Split the number into its digits
    digits = [int(digit) for digit in str(number)]
    
    # Calculate the sum of the cubes of its digits
    sum_of_cubes = sum(digit ** 3 for digit in digits)
    
    # Check if the sum of the cubes is equal to the number itself
    if sum_of_cubes == number:
        print("{}是水仙花数".format(number))
        return True
    else:
        print("{}不是水仙花数".format(number))
        return False
eval(input())
# Example usage:
# isSxh(153)  # This should print "153是水仙花数" and return True
# isSxh(103)  # This should print "103不是水仙花数" and return False