# Enter your code here. Read input from STDIN. Print output to STDOUT
# Using dynamic programming approach

def count_partitions(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1  # There is one way to partition 0 (the empty partition)

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions


T = int(input())
n = []
for _ in range(T):
    n.append(int(input()))
limit = max(n)
num_partitions = count_partitions(limit)
for num in n:
    print((num_partitions[num]-1) % (10**9 + 7))