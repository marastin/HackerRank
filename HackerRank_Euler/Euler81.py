# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
M = []
for i in range(N):
    L = list(map(int, input().split()))
    M.append(L)

n = N - 1
for i in range(n-1, -1, -1):
    M[n][i] += M[n][i+1]
    M[i][n] += M[i+1][n]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        M[i][j] += min(M[i+1][j], M[i][j+1])

print(M[0][0])