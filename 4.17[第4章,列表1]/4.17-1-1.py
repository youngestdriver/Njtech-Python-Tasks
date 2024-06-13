'''
假设有三个列表：lst_who=["小马","小羊","小鹿"]，lst_where=["草地上","电影院","家里"]，lst_what=["看电影","听故事","吃晚饭"]。
编写程序，由用户输入三个0~2之间的整数，将其作为索引分别访问三个列表中对应的元素并进行造句。
样例：
输入：1,0,2
输出：小羊在草地上吃晚饭
'''
lst_who = ['小马','小羊','小鹿']
lst_where = ['草地上','电影院','家里']
lst_what = ['看电影','听故事','吃晚饭']
a=eval(input())
who=a[0]
where=a[1]
what=a[2]

s=lst_who[who]+"在"+lst_where[where]+lst_what[what]
print(s)