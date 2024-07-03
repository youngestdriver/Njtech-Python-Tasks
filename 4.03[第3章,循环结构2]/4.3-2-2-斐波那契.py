#2. (程序题) 输出前n(n>=3)项的斐波那契数列。
#样例：
#输入：3
#输出：1,1,2
s=[1,1]
a=1
b=1
n=int(input())
for i in range(1,n-1):
    c=a+b
    s.append(c)
    a = b
    b = c

s_str = [str(num) for num in s] #列表推导式
print(','.join(s_str))
