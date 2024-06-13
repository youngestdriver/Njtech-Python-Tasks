'''
编写程序，使用列表存放n个学生的姓名和年龄，并将列表结果输出。n及学生的姓名和年龄由用户输入。
样例：
输入：
3
张三
18
李四
19
王二
20
输出：[['张三',18], ['李四',19], ['王二',20]]
'''

n = int(input())
students = []

for _ in range(n):
    name = input()
    age = int(input())
    students.append([name, age])  # 将姓名和年龄作为一个列表添加到students列表中

print(students)