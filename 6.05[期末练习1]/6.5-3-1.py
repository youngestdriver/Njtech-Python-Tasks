'''
杨辉三角, 是二项式系数在三角形中的一种几何排列。形如下图：

        1               n=1
      1   1             n=2
    1   2   1           n=3
  1   3   3   1         n=4
1   4   6   4   1       n=5

特点：
1、每行第1项为1
2、中间的每一项等于它上方两项之和
3、第n行有n项
试编写程序, 输出杨辉三角形的前n行。
样例：
输入：
3
输出：
[1]
[1, 1]
[1, 2, 1]
'''
n=int(input())
lst=[]
lstold=[]

for i in range(n):
    if i==0:
        lst=[1]
        lstold=lst[:]
        print(lst)

    elif i==1:
        lst=[1,1]
        lstold=lst[:]
        print(lst)

    else:
        lst=[]
        for a in range(i+1):
            if a==0 or a==i:
                lst.append(1)
            else:
                lst.append(lstold[a-1]+lstold[a])
        lstold=lst[:]
        print(lst)

    