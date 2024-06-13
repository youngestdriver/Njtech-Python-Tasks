'''
假设有列表lst_student存放了学生的基本信息，依次为学号、姓名和年龄。
试编写程序，根据用户输入学生姓名将其年龄输出。
列表内容也由用户输入。如果姓名不存在，则输出"姓名有误"。
样例：
输入：
["001","李梅",19,"002","刘祥",20,"003","张武",18]
刘祥
输出：20
'''
lst_student=eval(input())
name=input()

if name in lst_student:
    print(lst_student[lst_student.index(name)+1])

else:
    print("姓名有误")