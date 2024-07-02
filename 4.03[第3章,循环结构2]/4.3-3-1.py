#计算平均数
a=int(input())
b=0
count=0
while a!=0:
    count+=1
    b+=a
    avg=b/count
    a=int(input())
print("{:.2f}".format(avg)) #保留两位小数