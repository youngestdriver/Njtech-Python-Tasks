a=int(input())
count=0
sum_ji=0
sum_ou=0
while count!=9:
    if a%2!=0:
        sum_ji+=a
    if a%2==0:
        sum_ou+=a
    a=int(input())
    count+=1
print(sum_ji)
print(sum_ou)
#特奇怪，最后一位加不上。