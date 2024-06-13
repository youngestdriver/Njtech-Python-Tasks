'''
假设字符串s存放了某个学生某学期各门课程的期末考试成绩
（科目名称及数量不定，分数可以有小数，试编写程序，计算该学生所有科目的平均分
（利用format方法保留两位小数）。
样例：
输入（标点符号为中文形式）：
语文：80，数学：82，英语：90
输出：
84.00
'''
s = input()
subjects_scores = s.split("，")

total_score = 0
subject_count = 0

for subject_score in subjects_scores:
    subject, score = subject_score.split("：")
    total_score += float(score)
    subject_count += 1

average_score = total_score / subject_count
print("{:.2f}".format(average_score))