'''输出给定范围[a,b]的所有素数，一行3个。a和b的值由用户输入且均为正整数。
样例：
1
10
输出：
2 3 5 
7 '''
a=int(input())
b=int(input())
count = 0
for i in range(a,b+1):
    count += 1
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")
        if count % 3 == 0:
            print()

#count有问题，以及不能排除1这个非素数！