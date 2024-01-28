N = int(input())

n1 = 1
while True:
    ans = n1**N
    l1 = len(str(ans))
    if l1 == N:
        print(ans)
    elif l1 > N:
        break
    n1 += 1