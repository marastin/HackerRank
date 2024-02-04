from itertools import combinations
# Combinations are emitted in lexicographic sorted order. 
# So, if the input iterable is sorted, the combination tuples will be produced in sorted order.


print(list(combinations('12345',2)))

A = [1,1,3,3,3]
print(list(combinations(A,4)))



s = input().split()

S = sorted(s[0])
K = int(s[1])
for k in range(1, K + 1):
    for item in list(combinations(S, k)):
        print(''.join(item))
