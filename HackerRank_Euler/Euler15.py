from math import factorial

for _ in range(int(input())):
    n, m = map(int,input().split())
    result = (factorial(n+m)//factorial(n)//factorial(m))
    print(result % (10**9+7))