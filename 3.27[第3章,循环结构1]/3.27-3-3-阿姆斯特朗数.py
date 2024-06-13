#输出符合要求的阿姆斯特朗数。
#提示：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。n由用户输入。
#输出要求：数与数之间用空格隔开。
n = int(input())
armstrong_numbers = []

for i in range(10**(n-1),10**n):
    sum1=0
    i_copy = i
    while i_copy>0:
        num = i_copy%10
        sum1 += num**n
        i_copy //= 10
    if sum1 == i:
        armstrong_numbers.append(str(i))
print(' '.join(armstrong_numbers))

#妈的终于做对了，但是还有其他解法