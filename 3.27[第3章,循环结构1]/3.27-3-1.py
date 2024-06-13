#输出符合要求的阿姆斯特朗数。
#提示：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。n由用户输入。
#输出要求：数与数之间用空格隔开。
num = int(input())
armstrong_numbers = []

for i in range(1, num+1):
    n = len(str(i))
    temp = i
    sum1 = 0

    while temp > 0:
        digit = temp % 10
        sum1 += digit ** n
        temp //= 10
        
    if sum1 == i:
        armstrong_numbers.append(i)

print(*armstrong_numbers) #注意用end=会控制不了最后的空格，导致无法识别

#我趣！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#他妈的审错题了！！！！！是输出n位数中所有的Armstrong数，而不是1到n中