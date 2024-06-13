'''
有一堆桃子, 猴子每天吃桃子总数的一半并多吃一个, 吃了m天, 到m+1天只剩下了n个桃子。
试编写程序, 计算在猴子吃之前, 一共有多少个桃子? m和n的值由用户输入。
样例：
输入
3
1
输出
22
'''
def f(m,n):
    for i in range(m):
        n=(n+1)*2
    return(n)

print(f(int(input()),int(input())))