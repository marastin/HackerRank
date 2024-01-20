
N_max = 10 ** 5 + 1
sum_of_divisors = [1 for _ in range(N_max + 1)]
sum_of_divisors[0] = 0
sum_of_divisors[1] = 0
for number in range(2, N_max):
    for multiple in range(2 * number, N_max, number):
        sum_of_divisors[multiple] += number

sum_of_amicable = [0 for _ in range(N_max)]
current_sum = 0
for number in range(1, N_max):
    a = sum_of_divisors[number]
    if a < len(sum_of_divisors) and a != number:
        if sum_of_divisors[a] == number:
            current_sum += number
    sum_of_amicable[number] = current_sum

for _ in range(int(input())):
    n = int(input())
    print(sum_of_amicable[n-1])