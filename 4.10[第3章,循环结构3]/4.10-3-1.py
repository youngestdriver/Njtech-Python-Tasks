'''编写程序计算s=a+aa+aaa+...+aaa...aaa的值，
其中a是1~9之间的某个数字，n是一个正整数。a和n的值由用户输入。
样例：
输入：
2
5
输出：
s=2+22+222+2222+22222=24690'''
a=input ()
n=int (input ())
sum1=0
s="s="
for i in range(1,n+1):      
    shu=''
    for j in range(0,i):    #这个循环是在搭建 2+22+222
        shu += a
    s+=shu+"+"

    sum1 += int(shu)        #这是计算结果
    
print(s[:-1]+"="+str(sum1))

#不容易啊