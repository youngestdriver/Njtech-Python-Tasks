'''
假设已知电梯运行线路（用户输入），且已知初始楼层为2楼。试编写程序，将经过的楼层存放在列表中，并将列表输出。
样例：
输入：
↑↑↓↓↓↑↑↓↑↑↑↑
输出：
[2,3,4,3,2,1,2,3,2,3,4,5,6]
'''
a=input()
lst=[2]
count=-1
for n in a:
    if n=='↑':
        lst.append(lst[len(lst)-1]+1)
    else:
        lst.append(lst[len(lst)-1]-1)
print(lst)

