'''为了获知基因序列在功能和结构上的相似性，
经常需要将几条不同序列的 DNA 进行比对，
以判断该比对的 DNA 是否具有相关性。
现比对两条长度相同的 DNA 序列。
首先定义两条 DNA 序列相同位置的碱基为一个碱基对，
如果一个碱基对中的两个碱基相同的话，
则称为相同碱基对。接着计算相同碱基对占总碱基对数量的比例，
如果该比例大于等于给定阈值时则判定该两条 DNA 序列是相关的，
否则不相关。
输入输出格式：
输入：有三行，第一行是用来判定出两条 DNA 序列是否相关的阈值，
随后两行是两条 DNA 序列（长度相同）
输出：若两条 DNA 序列相关，则输出 yes，否则输出no。
样例：
输入：
0.85
ATCGCCGTAAGTAACGGTTTTAAATAGGCC
ATCGCCGGAAGTAACGGTCTTAAATAGGCC
输出：
yes'''
percent=eval(input())
DNA1=input()
DNA2=input()
count=0
for i in range (0,len(DNA1)):
    if DNA1[i]==DNA2[i]:
        count+=1
percent_over=count/len(DNA1)
if percent_over>=percent:
    print("yes")
else:
    print("no")