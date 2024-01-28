# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    N = int(input())
    M = []
    for i in range(N):
        L = list(map(int, input().split()))
        M.append(L)

    n = N - 1

    for i in range(n-1, -1, -1):
        for j in range(len(M[i])):
            M[i][j] += max(M[i+1][j], M[i+1][j+1])

    print(M[0][0])