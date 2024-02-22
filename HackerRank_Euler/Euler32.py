from itertools import permutations
from time import time

t1 = time()

N = 9
lst = ''.join([str(i) for i in range(1,N+1)])
Perm = permutations(lst)
ans_set = set()
for P in Perm:
    P = ''.join(P)
    for s1 in range(1, max(3,N-4)):
        for s2 in range(s1 + 1, max(4, N-3)):
            a = int(P[0:s1])
            b = int(P[s1:s2])
            c = int(P[s2:])
            if a * b == c:
                print((a, b, c))
                ans_set.add(c)

print(sum(ans_set))
print(f"time: {time()-t1:.3f} sec")
