T = int(input())
for _ in range(T):
    x = int(input())
    a = (-1 + (1 + 8*x)**0.5)/2
    if a - int(a):
        print(-1)
    else:
        print(int(a))