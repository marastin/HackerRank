
# Method 1
from decimal import Decimal, getcontext
getcontext().prec = 400


T = int(input())

for _ in range(T):
    n = Decimal(input())
    
    if n == 1:
        print(1)
    else:
        m = (n-1)/2
        ans = (1 + 8*m*(m+1)*(2*m+1)//3 + 2*m*(m+1) +4*m)%(10**9 + 7)
        print(int(ans))


# Method 2
# def size_of_spiral(n: int) -> int:
#     s = (4*n*(n+1)*(2*n+1)//6+n*(n+1)//2+n+1)*4-4+1;
#     return s % (10**9+7)
    
# for _ in range(int(input())):
#     print(size_of_spiral(int(input())//2))