'''
试编写程序，统计给定的一段英文文本中出现频率最高的三个字母
（按照频率从高到低排列）。
样例：
输入：
In the future, China's medical system will shift its focus from basic digitalization to clinical digitalization that centers on patients, the report said.
输出：
i
t
a
'''
s="In the future, China's medical system will shift its focus from basic digitalization to clinical digitalization that centers on patients, the report said."
s_low=s.lower()

count={}
for w in s_low:
    if w not in [' ',"'",',','.']:
        if w in count:
            count[w]=count[w]+1
        else:
            count[w]=1
# lsVK=[(v,k) for k,v in count.items()]
# lsVK.sort()
# lsKV=[(k,v) for v,k in lsVK]

count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word, freq in count_sorted[:3]:
    print(word)

