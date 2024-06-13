'''
5、每个偶数（>=4）都能由两个素数相加得到。输出给定范围内每个偶数拆分成两个素数之和（具体格式见样例）的式子。
样例：
4
10
4=2+2
6=3+3
8=3+5
10=3+7
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(start, end):
    if start % 2 == 0:
        for even_num in range(start, end+1, 2):
            for i in range(2, even_num//2+1):
                if is_prime(i) and is_prime(even_num - i):
                    print("{}={}+{}".format(even_num, i, even_num - i))
                    break
    else:
        for even_num in range(start+1, end+1, 2):
            for i in range(2, even_num//2+1):
                if is_prime(i) and is_prime(even_num - i):
                    print("{}={}+{}".format(even_num, i, even_num - i))
                    break

start_value = int(input()) # "Enter the starting value (greater than 2): "
end_value = int(input()) # "Enter the ending value: "
find_prime_pairs(start_value, end_value)
