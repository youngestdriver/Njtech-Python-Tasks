'''
输出范围[a,b]所有符合要求的整数。
a和b的值均为正整数，且均由用户输入。
1、必须是素数
2、必须是回文数
样例：
输入：
100
150
输出：
101
131
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_prime_palindromes(a, b):
    result = []
    for num in range(a, b + 1):
        if is_prime(num) and is_palindrome(num):
            result.append(num)
    return result

def main():
    a = int(input())
    b = int(input())
    prime_palindromes = find_prime_palindromes(a, b)
    for num in prime_palindromes:
        print(num)

if __name__ == "__main__":
    main()