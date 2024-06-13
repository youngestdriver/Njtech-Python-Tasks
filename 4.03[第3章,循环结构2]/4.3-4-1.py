n = int(input())

for i in range(10**n,10**(n-1),-1):
    sum1=0
    i_copy = i
    while i_copy>0:
        num = i_copy%10
        sum1 += num**n
        i_copy //= 10
    if sum1==i:
        break
print(i)