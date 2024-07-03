'''输出给定范围[a,b]的所有素数，一行3个。a和b的值由用户输入且均为正整数。
样例：
1
10
输出：
2 3 5 
7 '''
a = int(input())
b = int(input())
count = 0  # 用于计数已打印的素数数量
for i in range(a, b + 1):
    # 1 不是素数，直接跳过
    if i < 2:
        continue
    for j in range(2, i):  # 只需检查到sqrt(i)即可 #啊啊啊啊啊啊注意不是i+1，不然就会对自己取余，全没了！！
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        count += 1
        if count % 3 == 0:
            print()  # 每打印3个**素数**就换行

#太妙了！ 不愧是AI啊，吾不及也。