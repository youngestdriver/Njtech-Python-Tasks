'''
编写程序，输出某年某月的天数，某年某月由用户数输入。
（1）创建一个列表，依次存放当年每个月对应的天数。
（2）需要考虑闰年的情况。
样例：
输入：2024-2
输出：29
'''
date=input() #”2024-2"

date_lst=date.split("-") #检索"-"两边的内容，并分别放入列表内
year=int(date_lst[0])
month=int(date_lst[1])

month2=28
if year%400==0 or (year%4==0 and year%100!=0):
    month2=29

lst=[31,month2,31,30,31,30,31,31,30,31,30,31]
print(lst[month-1])
