'''
假设有列表lst_student存放了学生的基本信息，依次为学号、姓名和年龄。
试编写程序，根据用户输入学生姓名将其年龄输出。
列表内容也由用户输入。如果姓名不存在，则输出"姓名有误"。
样例：
输入：
[["001","李梅",19],["002","刘祥",20],["003","张武",18]]
刘祥
输出：
20
'''
lst_student=eval(input())
name=input()

for list_every in lst_student:
    if name in list_every:
        # print(list_every[list_every.index(name)+1])
        print(name[-1]) # 不需要那么麻烦👆
        break

else: # 等到遍历完所有列表中的每个列表中的姓名，如果还没有，则姓名有误
    print("姓名有误")