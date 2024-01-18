def sum_of_digits_2_to_n(n):
    result = pow(2, n)
    digit_sum = sum(int(digit) for digit in str(result))
    return digit_sum

for _ in range(int(input())):
    n = int(input())
    result_sum = sum_of_digits_2_to_n(n)
    print(result_sum)