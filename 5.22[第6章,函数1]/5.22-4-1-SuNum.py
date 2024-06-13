'''
4、输出给定范围内的孪生素数（值相差为2的两个素数称为孪生素数）。范围的起始值和终止值由用户输入。
样例：
输入：
1
10
输出：
3 5
5 7
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end - 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

start = int(input())
end = int(input())

result = find_twin_primes(start, end)
# print("Twin primes within the range are:")
for twin_prime in result:
    print(twin_prime[0], twin_prime[1])
