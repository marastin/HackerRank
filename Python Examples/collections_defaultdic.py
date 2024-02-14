from collections import defaultdict

# Example 1
d = defaultdict(list)
d['python'].append("awesome") # a defaultdict will have a default value if that key has not been set yet
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)




# HackerRank
d = defaultdict(list)

n, m = map(int, input().split())
for idx in range(n):
    s = input()
    d[s].append(idx+1)
for idx in range(m):
    s = input()
    if not d[s]:
        d[s].append(-1)
    print(' '.join(map(str, d[s])))