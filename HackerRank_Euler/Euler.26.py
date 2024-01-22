# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_recurring_digits(numerator, denominator):
    seen_remainders = {}
    result = []

    remainder = numerator % denominator

    while remainder != 0 and remainder not in seen_remainders:
        seen_remainders[remainder] = len(result)
        remainder *= 10
        result_digit = remainder // denominator
        result.append(result_digit)
        remainder %= denominator

    if remainder == 0:
        recurring_digits = []
    else:
        recurring_digits = result[seen_remainders[remainder]:]

    return recurring_digits



T = int(input())
n = []
for _ in range(T):
    n.append(int(input()))

n_recurring = [0, 0]
for i in range(2, max(n)+1):
    n_recurring.append(len(find_recurring_digits(1, i)))


for idx in n:
    max_val = max(n_recurring[:idx])
    n_recurring[:idx+1].index(max_val)
    print(n_recurring[:idx+1].index(max_val))