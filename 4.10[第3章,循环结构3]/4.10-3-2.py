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
b=''
s=0
st='s='

for i in range (1, n+1) :
    b=b+a
    s+=int(b)
    st+=b+'+'
#print (st[:-1],'=',s) 注意这里用逗号相隔会出现等号与两个数之间有空格
#print (st[:-1]+'='+s) 注意s为int 其余的为str 不能进行字符串运算
print (st[:-1],'=',str(s))