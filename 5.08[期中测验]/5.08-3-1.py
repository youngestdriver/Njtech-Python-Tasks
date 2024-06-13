'''
编写程序计算1*3*5 + 3*5*7 + 5*7*9 + ... +n*(n+2)*(n+4)的值
n(n为奇数)的值由用户输入。
样例：
输入：
3
输出：
1*3*5+3*5*7=120
'''
n=int(input())
sum1=0
lst=[]
for i in range(1,n+1,2):
    sum1+=i*(i+2)*(i+4)
for i in range(1,n+1,2):
    lst.append(str(i)+"*"+str(i+2)+"*"+str(i+4))
print("+".join(lst)+"="+str(sum1))