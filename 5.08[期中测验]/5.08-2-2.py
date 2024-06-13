'''
输出n位正整数中最大的阿姆斯特朗数。
提示：如果一个n位正整数等于其各位数字的n次方之和,
则称该数为阿姆斯特朗数。n由用户输入。
样例：
输入：
3
输出：
407
'''
n = int(input())
armstrong_number=""

for i in range(10**n,10**(n-1),-1):
    sum1=0
    i_copy = i
    while i_copy>0:
        num = i_copy%10
        sum1 += num**n
        i_copy //= 10
    if sum1 == i:
        armstrong_number=i
        break
print(armstrong_number)
    