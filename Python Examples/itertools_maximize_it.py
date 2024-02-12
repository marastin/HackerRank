# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

f = lambda x: x**2

K, M = map(int, input().split())
L = []
for idx in range(K):
    L.append(list(map(int, input().split()))[1:])

p = product(*L)
Smax = -1
for item in p:
    Smax = max(Smax, sum(map(f, item)) % M)

print(Smax)