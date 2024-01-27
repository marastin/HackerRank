# Enter your code here. Read input from STDIN. Print output to STDOUT

Roman_num = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def to_digit(num_str):
    n = 0
    for (s, v) in Roman_num:
        L = len(num_str)
        num_str = num_str.replace(s, '')
        n += (L - len(num_str)) * v // len(s)
    return n

def to_roman(num):
    ans = ''
    for s, v in Roman_num:
        ans += num // v * s
        num -= num // v * v
    return ans

T = int(input())

for _ in range(T):
    print(to_roman(to_digit(input())))