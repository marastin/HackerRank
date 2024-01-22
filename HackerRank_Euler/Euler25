from decimal import Decimal, getcontext

getcontext().prec = 5002

fib = [Decimal(1), Decimal(1)]
n_dig = [0, 1]

index = 2
max_len = 2

while max_len <= 5001:
    new_fib = fib[0] + fib[1]
    index += 1
    fib[0], fib[1] = fib[1], new_fib
    L = len(str(new_fib))
    if L == max_len:
        n_dig.append(index)
        max_len += 1
        
T = int(input())
for _ in range(T):
    n = int(input())
    print(n_dig[n])