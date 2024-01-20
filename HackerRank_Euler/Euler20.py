import math

for _ in range(int(input())):
    n = int(input())
    s = str(math.factorial(n))
    print(sum([int(dig) for dig in s]))