# Enter your code here. Read input from STDIN. Print output to STDOUT

def last_10_digits_of_series(N):
    total_sum = 0
    modulo = 10**10

    for i in range(1, N+1):
        total_sum = (total_sum + pow(i, i, modulo)) % modulo

    return total_sum

N = int(input())
result = last_10_digits_of_series(N)
print(result)
