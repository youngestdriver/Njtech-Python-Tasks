'''
斐波那契数列又称黄金分割数列、兔子数列，其第1、2项均为1，从第3项开始每一项都是前两项之和，即1，1，2，3，5，8，13，21，34，……。试编写程序，
利用列表计算斐波那契数列前n项。并将列表输出。n(n>=2)由用户输入。
样例：
输入：
10
输出：
[1,1,2,3,5,8,13,21,34,55]
'''
n=int(input())
lst=[1,1]
for i in range(1,n-1):
    lst_1=lst[-1]
    lst_2=lst[-2]
    lst_new=lst_1+lst_2
    lst.append(lst_new)
print(lst)