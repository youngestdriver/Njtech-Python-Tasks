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
n=int(input())
for num in range(10**n,10**n-1,-1):
    sum1=0
    for i in range(1,n+1):
        sum1+=(num%10)**n
        sum1//=10
        print(sum1)
        print(num)
    if sum1==num:
        break
    