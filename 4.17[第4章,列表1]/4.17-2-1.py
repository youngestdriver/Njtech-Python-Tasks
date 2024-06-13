'''
编写程序，输出某年某月的天数，某年某月由用户数输入。
（1）创建一个列表，依次存放当年每个月对应的天数。
（2）需要考虑闰年的情况。
样例：
输入：2024-2
输出：29
'''
a=str(input())
b=a.index('-') #我直接索引中间的“-”符号位置
year=int(a[0:b])
month=int(a[b+1:])

if year%400 == 0 or year%100 == 0 and year %4 != 0: #筛选是否为闰年
    month_run=[31,29,31,30,31,30,31,31,30,31,30,31]
    print(month_run[month-1])
else:
    month_not=[31,28,31,30,31,30,31,31,30,31,30,31]
    print(month_not[month-1])