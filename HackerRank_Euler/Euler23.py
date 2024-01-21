# Enter your code here. Read input from STDIN. Print output to STDOUT

N_max = 10 ** 5 + 1
sum_of_divisors = [1 for _ in range(N_max + 1)]
sum_of_divisors[0] = 0
sum_of_divisors[1] = 0
for number in range(2, N_max):
    for multiple in range(2 * number, N_max, number):
        sum_of_divisors[multiple] += number

abundant_nums = []
for idx, num in enumerate(sum_of_divisors):
    if idx < num:
        abundant_nums.append(idx)

def can_be_writen_as_sum_of_two_abundant(n, abundant_nums=abundant_nums):
    idx = 0
    x = abundant_nums[idx]
    while x < n//2 + 1:
        y = n - x
        if y in abundant_nums:
            return "YES"
        idx += 1
        x = abundant_nums[idx+1]
    return "NO"

T = int(input())
for _ in range(T):
    n = int(input())
    print(can_be_writen_as_sum_of_two_abundant(n))