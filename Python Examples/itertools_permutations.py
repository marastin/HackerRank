from itertools import permutations

print(permutations(['1','2','3']))
print(list(permutations(['1','2','3'])))
print(list(permutations(['1','2','3'], 2)))
print(list(permutations('abc', 3)))


s = input().split()

S = s[0]
K = int(s[1])
for item in sorted(list(permutations(S, K))):
    print(''.join(item))
