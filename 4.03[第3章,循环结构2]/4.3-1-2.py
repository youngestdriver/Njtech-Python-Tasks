ji_sum = 0
ou_sum = 0

for i in range(10):
    number = int(input())
    if number % 2 == 0:
        ou_sum += number
    else:
        ji_sum += number

print(ji_sum)
print(ou_sum)
#这样就好了…range循环简单多了