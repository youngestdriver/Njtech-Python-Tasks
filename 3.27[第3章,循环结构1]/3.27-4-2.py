#输出1-n内所有的回文数。n由用户输入。
#提示：设m是一任意自然数。若将m的各位数字反向排列所得自然数m1与m相等，则称m为一回文数。
#例如，若m=1234321，则称m为一回文数；但若m=1234567，则m不是回文数。
#输出格式要求：数与数之间用逗号隔开
#样例：
#输入：10
#输出:1,2,3,4,5,6,7,8,9
n=int(input())
s=""

for i in range (1, n+1):
    j=str(i)
    if j==j[::-1]:
        s=s+j+','
print (s[:-1])