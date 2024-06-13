'''
输入一个整数列表 ls 和整数 m ，按顺序实现如下功能：

1）将列表 ls 中所有比 m 大的元素变为原来的2倍，所有比 m 小的元素变为原来的3倍，
与 m 相等的元素保持不变，然后输出变化后的列表。
2）计算并输出变化后列表的方差var(小数位数保留2位)，方差var的计算公式如下：
https://img96.pixhost.to/images/315/477460969_snipaste_2024-06-12_09-08-28.png
其中 n 表示列表元素的个数，表示列表的某个元素，表示列表所有元素的平均值，表示累加求和。

输入输出格式说明：
输入：
一共两行。第一行为列表格式的整数序列 ls；第二行为一个整数，表示 m 。
输出：
一共两行。第一行为处理后变化的列表，第二行为变化后列表的方差。

输入输出样例：
输入：
[5, 4, 3, 1, 2, 6, 7, 8, 9, 0]
5
输出：
[5, 12, 9, 3, 6, 12, 14, 16, 18, 0]
34.72
'''
def FangCha(ls, m):
    # 1. 修改列表
    modified_ls = []
    for x in ls:
        if int(x) > m:
            modified_ls.append(x * 2)
        elif int(x) < m:
            modified_ls.append(x * 3)
        else:
            modified_ls.append(x)
    
    # 2. 计算方差
    n = len(modified_ls)
    mean = sum(modified_ls) / n
    var = sum((x - mean) ** 2 for x in modified_ls) / (n - 1)
    var = round(var, 2)
    
    return modified_ls, var

# 输入
ls = eval(input())
m = int(input())

# 处理并计算方差
modified_ls, var = FangCha(ls, m)

# 输出
print(modified_ls)
print(var)
