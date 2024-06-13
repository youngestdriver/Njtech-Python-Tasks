'''
假设已有列表lst_floor(内容由用户输入)，存放了某电梯在一段时间内经过的楼层。试编写程序，输出电梯的运行线路。
符号"↑"表示上行一层，"↓"表示下行一层。
样例：
输入：
[1,4,2,5,7,3]
输出：
↑↑↑↓↓↑↑↑↑↑↓↓↓↓
'''
lst=eval(input())
for i in range(1,len(lst)):
    lst_1=lst[i-1]
    lst_2=lst[i]
    cha_zhi=lst_2-lst_1
    if cha_zhi>0:
        print("↑"*cha_zhi,end="")
    else:
        print("↓"*(-1*cha_zhi),end='')