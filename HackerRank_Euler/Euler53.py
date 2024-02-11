from math import comb

n, k = map(int, input().split())

count = 0
for i in range(n+1):
    for j in range(1, i+1):
        if comb(i, j) > k:
            count += 1

print(count)