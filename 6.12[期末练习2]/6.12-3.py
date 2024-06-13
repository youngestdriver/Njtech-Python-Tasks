'''
输入一个字典，字典中存放了三门课程参加考试的学生的分数，
要求将每门课程的平均分添加到分数列表的最后并按样例输出结果，平均分使用round函数保留一位小数。
【提示：输入字典使用d=eval(input())】
输入输出样例如下：

输入
{'语文':[85,89,76,88],'数学':[88,92,96],'英语':[98,90,95,99,92]}

输出：

语文科目参加考试人数为4均分为84.5
数学科目参加考试人数为3均分为92.0
英语科目参加考试人数为5均分为94.8
{'语文': [85, 89, 76, 88, 84.5], '数学': [88, 92, 96, 92.0], '英语': [98, 90, 95, 99, 92, 94.8]}
'''
# 输入字典
d = eval(input())

for subject, scores in d.items():                       # 处理每门课程的分数
    
    avg_score = round(sum(scores) / len(scores), 1)     # 计算平均分
    
    scores.append(avg_score)                            # 添加平均分到分数列表的最后
    
    print("{}科目参加考试人数为{}均分为{}".format(subject,len(scores) - 1,avg_score)) 

print(d)

