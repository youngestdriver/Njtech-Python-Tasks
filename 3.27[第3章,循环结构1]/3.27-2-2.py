n = int(input())
count = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")
        count += 1
        if count % 3 == 0:
            print()