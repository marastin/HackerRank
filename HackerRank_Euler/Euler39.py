from math import gcd

"""
The problem you're referring to is a classic example of a Pythagorean triple.
p > q
p - q is odd

a = p^2 - q^2
b = 2*p*q
c = p^2 - q^2

"""

def solve(limit):
    result = [0]*(limit + 1)
    L1 = int((limit // 2)**0.5) + 1
    combs = [(p, q) for p in range(1, L1) for q in range(1, p) if (p - q) % 2 == 1 and gcd(p,q) == 1]
    # print(combs)
    for (p, q) in combs:
        s = 2*p**2 + 2*p*q
        if s < limit + 1:
            multi = limit//s
            for i in range(1, multi + 1):
                result[s*i] += 1
    

    max_result = [0]*(limit + 1)
    maxi = 0
    for i in range(1, limit+1):
        if result[i] > maxi:
            max_result[i] = i
            maxi = result[i]
        else:
            max_result[i] = max_result[i-1]
    return max_result


T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))

limit = max(N)

max_result = solve(limit)

for n in N:
    print(max_result[n])