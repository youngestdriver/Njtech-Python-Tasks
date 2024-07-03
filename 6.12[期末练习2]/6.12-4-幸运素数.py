'''
如果一个数本身是素数，并且把最低位删除后得到的数仍是素数、再把最低位删除后得到的数仍是素数……
如此往复,直到得到一个一位素数,我们就称它是“幸运素数”。
以233为例:
233 本身是素数；23 = [233/10] 是素数；2  = [23/10]是素数，
因此 233 是“幸运”素数。而211 则不是幸运素数：虽然 211 是素数,但 21 不是素数。
请编程,求出一定范围内的所有幸运数字:

输入输出示例:
输入区间起点值与终点值
6
30
输出区间内幸运素数
7
23
29
'''
# def is_prime(n):
#     """判断一个数是否为素数"""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lucky_prime(n):
    """判断一个数是否为幸运素数"""
    while n > 0:
        if not is_prime(n):
            return False
        else:                   #这里的else甚至可以省略
            n //= 10
    return True

def find_lucky_primes(start, end):
    """找到给定区间内的所有幸运素数"""
    lucky_primes = []
    for num in range(start, end + 1):
        if is_lucky_prime(num):
            lucky_primes.append(num)
    return lucky_primes

# 获取输入
start = int(input())
end = int(input())

# 查找幸运素数
lucky_primes = find_lucky_primes(start, end)

# 输出结果
for prime in lucky_primes:
    print(prime)
