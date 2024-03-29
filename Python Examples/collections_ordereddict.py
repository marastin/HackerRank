# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


# Example 1 - HackerRank
# Syntax 1
N = int(input())
OD = OrderedDict()
for _ in range(N):
    S = input().split()
    name = ' '.join(S[:-1])
    net_price = int(S[-1])
    if name in OD:
        OD[name] += net_price
    else:
        OD[name] = net_price

for item in OD:
    print(item, OD[item])


# Syntax 2
OD = OrderedDict()
for _ in range(int(input())):
    name, net_price = input().rsplit(maxsplit=1)
    OD[name] = OD.get(name, 0) + int(net_price)
for item in OD.items():
    print(*item)



# Example 2 - HackerRank Word Order

OD = OrderedDict()
for _ in range(int(input())):
    word = input()
    OD[word] = OD.get(word, 0) + 1

print(len(OD))

for item in OD.items():
    print(item[1], end=' ')